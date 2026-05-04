# Active Directory Fundamentals

This document covers the theory that frames the rest of the lab — the architecture and authentication protocols that the build sections ([02](02-domain-controller.md) – [05](05-powershell-automation.md)) implement, and the security context that makes those implementations relevant to SOC analyst work.

The build documents focus on *what was configured*. This one focuses on *why those configurations matter*, particularly from the perspective of an analyst investigating authentication-based attacks, lateral movement, or privilege escalation in a Windows environment.

---

## Career framing

This lab sits alongside ten years of operational identity and access management (IAM) experience in a federal government environment — daily user lifecycle work, authentication troubleshooting, access control enforcement across roughly 100 user accounts. That operational depth provided the *what does identity work look like in production* context. What it didn't provide was hands-on configuration of the underlying AD infrastructure that powered those operations.

This lab closes that gap. The combination — extensive operational IAM experience plus hands-on AD technical configuration — is the foundation for transitioning into identity-focused security operations roles, where the same authentication mechanisms that legitimate users rely on are exactly what attackers abuse.

---

## Security principals

Active Directory manages three types of objects that can authenticate and be granted privileges. Each has distinct properties and a distinct attack surface.

### Users

The most common AD object. Two functional sub-types:

- **People accounts** — employees and contractors who log in interactively
- **Service accounts** — used by applications (IIS, SQL Server, scheduled tasks) to authenticate non-interactively

The lifecycle is the same for both: created, modified over time, disabled, eventually deleted. The security implication is also the same: every user account is a potential authentication target. Compromising any account gives an attacker a foothold; compromising a privileged account gives them substantially more.

### Machine accounts

Every computer joining a domain receives a machine account, named with the computer name plus a dollar sign (`DC01$`, `WORKSTATION01$`). These accounts are full security principals — they authenticate, they hold privileges, they appear in event logs.

A few properties make them notable from a security perspective:

- Their passwords are 120 random characters and rotate automatically every 30 days
- They have local administrator rights on their assigned computer (and only their assigned computer)
- They're often overlooked in security monitoring because they're "just computers"

Compromising a machine account enables specific attack patterns: pass-the-hash using machine credentials, lateral movement to systems where the machine has admin rights, and (if the machine is a service host) silver ticket attacks against services running under that account.

### Groups

Collections of users, computers, or other groups, used for bulk permission assignment. A user can belong to many groups; group membership is the primary mechanism for resource access in AD.

Several built-in groups carry significant default privileges:

| Group | Privilege scope | Why it matters to security |
|-------|----------------|---------------------------|
| **Domain Admins** | Full administrative control over every computer in the domain | The primary credential-theft target — compromise = domain ownership |
| **Enterprise Admins** | Administrative control across the entire forest | Higher than Domain Admins; multi-domain attack pivot |
| **Server Operators** | Can administer domain controllers but not modify admin groups | Often overlooked; sufficient to weaken DC security |
| **Backup Operators** | Can read any file regardless of NTFS permissions (for backup purposes) | Valuable for data exfiltration; bypasses ACLs |
| **Account Operators** | Can create and modify user accounts in the domain | Sufficient to create persistent backdoor accounts |
| **Domain Users** | Default group containing every user account | Membership is non-privileged but useful for enumeration |

The principle: **default group membership matters as much as explicit grants.** A user who is "just" a member of Backup Operators has effective access to every file in the environment, even though no individual file ACL says so.

---

## Organizational units and groups (briefly)

The mechanics of OUs and security groups are documented in [03 — Identity Structure](03-identity-structure.md). The security-relevant summary is short:

- **OUs** determine what policies apply (via GPO linkage) and who can administer subsets of the directory (via delegation). They define the *administrative blast radius* — what an admin scoped to a particular OU can affect.
- **Security groups** determine what resources a user can reach. They define the *access blast radius* — what data and systems a compromised account can reach.

Healthy directories keep these two boundaries aligned with business reality. Compromised directories drift apart: users with stale group memberships from old roles, OU structures that no longer match the org chart, and delegated admins who outlive the projects that justified their access.

---

## Authentication protocols

Understanding Kerberos and NetNTLM is the single most useful technical skill for analyzing authentication-based attacks. Both protocols generate Windows event logs that SIEM platforms ingest; both have specific attack patterns that are only detectable if the analyst understands the underlying flow.

### Kerberos: ticket-based authentication

Kerberos authenticates users to services without ever transmitting the user's password (or its hash) across the network. It does this through a three-phase ticket exchange involving the **Key Distribution Center (KDC)** — a service running on every domain controller.

**Phase 1 — TGT request (initial authentication):**

```
User → KDC:    Username + timestamp encrypted with the user's password-derived key
KDC → User:    Ticket Granting Ticket (TGT), encrypted with the krbtgt account hash
               + a Session Key for future requests
```

The TGT is the user's proof of having authenticated. It does *not* contain the password; it contains an encrypted assertion that the KDC verified the user's identity. The TGT is encrypted using the hash of a special account named `krbtgt`, which exists on every DC for exactly this purpose.

**Phase 2 — TGS request (service access):**

```
User → KDC:    TGT + Service Principal Name (SPN) + timestamp encrypted with Session Key
KDC → User:    Ticket Granting Service ticket (TGS), encrypted with the service owner's hash
               + a Service Session Key
```

A TGS grants access to one specific service. To access multiple services, a user requests multiple TGSs (each authenticated by the same TGT). The TGS is encrypted with the *service account's* password hash, which means the receiving service can decrypt it.

**Phase 3 — service authentication:**

```
User → Service:  TGS + authenticator encrypted with Service Session Key
Service:         Decrypts TGS using its own password hash → extracts Service Session Key
                 → validates authenticator → grants access
```

The service never contacts the KDC during this phase. It validates the user purely by demonstrating that the encrypted TGS could only have been issued by a KDC that knows both the user's identity and the service's password hash.

### Kerberos attack surface

The same mechanics that make Kerberos secure when keys are protected make it devastating when keys are stolen. Five attack patterns are the core of what SOC analysts look for:

| Attack | Target | Effect |
|--------|--------|--------|
| **Golden Ticket** | `krbtgt` account hash | Forge TGTs for any user, including non-existent accounts; persistent domain compromise |
| **Silver Ticket** | A specific service account hash | Forge TGSs for that one service; stealthy because no KDC interaction is required |
| **Kerberoasting** | Service accounts with weak passwords | Request TGSs for service accounts, crack their password hashes offline |
| **Pass-the-Ticket** | A stolen TGT or TGS | Reuse a valid ticket on another machine without needing the user's password |
| **Overpass-the-Hash** | A user's NTLM hash | Use the hash to request a Kerberos TGT, bridging from NTLM compromise to Kerberos access |

The detection patterns for each of these attacks live in Windows Security event logs — primarily Event ID 4768 (TGT request) and Event ID 4769 (TGS request). Analyzing those events meaningfully requires understanding what a *legitimate* TGT/TGS exchange looks like, which is what the protocol breakdown above provides.

### NetNTLM: legacy challenge-response

NetNTLM predates Kerberos and remains in use for backward compatibility. The flow is simpler:

```
1. Client → Server:           Authentication request
2. Server → Client:           Random challenge value
3. Client:                    Combines NTLM hash + challenge → response
4. Client → Server:           Response
5. Server → DC:               Forwards challenge + response for validation
6. DC:                        Recalculates expected response, compares with received
7. DC → Server:               Authentication result
8. Server → Client:           Access granted/denied
```

NetNTLM has two security weaknesses worth knowing:

- **No mutual authentication.** The client trusts the server based on the network connection alone. There's no cryptographic proof that the server is the one the client intended to reach.
- **Susceptible to relay.** An attacker who intercepts the challenge/response exchange can forward it to a different service, authenticating *as the victim* to a system the victim never intended to contact. This is the classic NTLM Relay attack.

Mitigations exist — SMB signing, LDAP signing, Extended Protection for Authentication — but they're configuration-dependent and frequently disabled in environments that prioritize compatibility over hardening.

---

## Enterprise architecture: trees, forests, and trusts

Single-domain environments like the lab are the simplest case. Real enterprises often span multiple domains, organized into trees and forests, connected by trust relationships. The terminology is worth knowing because trust boundaries are also security boundaries — and because attackers explicitly enumerate and exploit trust relationships during lateral movement.

### Trees

A **tree** is a hierarchy of domains sharing a contiguous DNS namespace. Example:

```
thm.local                  ← root domain
├── uk.thm.local           ← child domain (UK operations)
├── us.thm.local           ← child domain (US operations)
└── asia.thm.local         ← child domain (Asia-Pacific)
```

Each child domain has its own DCs, its own Domain Admins (scoped to that domain), and its own user/computer objects. **Enterprise Admins** is the only built-in group with control across the entire tree.

This structure is common in geographically distributed organizations where regional IT teams need administrative autonomy but the business operates as a single entity.

### Forests

A **forest** is one or more trees sharing a common configuration and schema, but with potentially independent namespaces. Example: a company merger.

```
Forest
├── Tree 1: thm.local       ← original company
│   ├── uk.thm.local
│   └── us.thm.local
└── Tree 2: mht.local       ← acquired company
    ├── eu.mht.local
    └── asia.mht.local
```

Forests are used when organizations need to share resources across completely separate namespaces — typically post-merger, or in cases where regulatory requirements demand strict naming separation.

### Trust relationships

Trusts are the mechanism that lets a user from one domain authenticate to resources in another. The directionality is counter-intuitive:

> **Trust direction is opposite of access direction.** If Domain A trusts Domain B, users in Domain B can be authorized in Domain A — *not the reverse*.

```
Domain A ----trusts----> Domain B

Result: B's users may access A's resources
        A's users CANNOT access B's resources
```

A two-way trust (the default between domains in the same tree or forest) lets users from either side access resources on the other.

Three properties of trusts have direct security implications:

1. **Trust enables authorization, not access.** A trust lets `B\Alice` *authenticate* to a server in domain A. Whether she can actually open files on that server still depends on the file's ACL granting her permissions.
2. **Trusts are attack pivots.** Once an attacker compromises a low-privilege account in one domain, trust enumeration reveals which other domains they can pivot into.
3. **SID History injection** — the technique of adding a privileged SID from one domain to a user crossing a trust — is a documented attack pattern when trusts are configured without selective authentication.

---

## Integration with security operations

The point of building a deep theoretical understanding of AD isn't to administer AD better (though it helps). It's to recognize the difference between legitimate AD activity and malicious activity in the same logs.

### Detecting lateral movement

A SIEM alert: *"Multiple authentication attempts from a single source to multiple destinations on port 445 (SMB)."*

Without AD context, this alert is ambiguous — it could be a domain admin running a legitimate maintenance script, a backup process, or an attacker spreading laterally. With AD context, the analyst can ask:

- **What kind of account is the source?** A user account behaving this way is suspicious; a machine account behaving this way could be either a malware-infected workstation or a legitimate service.
- **What privileges does it hold?** Membership in Domain Admins makes the account a high-value target *and* makes legitimate fan-out activity more plausible. Service accounts with broad SMB rights are common Kerberoasting victims.
- **What protocol is in use?** Kerberos events (4768, 4769) versus NTLM events (4776) suggest different attack patterns — Kerberos lateral movement often involves stolen tickets; NTLM lateral movement often involves relay attacks.

The same log entries support different conclusions depending on the directory context the analyst can apply to them.

### Detecting privilege escalation

A SIEM alert: *"User account added to a privileged group."*

The follow-up questions an AD-literate analyst asks:

- **Which group?** Domain Admins is critical; Account Operators is a backdoor-creation enabler; Backup Operators is a data-exfiltration enabler. Each demands different urgency.
- **Who made the change?** A change made by a Domain Admin account is plausible (verify the admin); a change made by a regular user account is structurally impossible (vulnerability or compromise) and warrants immediate investigation.
- **From what system?** A change originating on a domain controller via standard administrative tooling is expected. A change originating on a workstation via remote admin tools should be verified. A change originating from outside the domain is an external attack.
- **At what time?** Business hours, with calendar context for the admin, suggests legitimate work. 3 AM on a Sunday with no maintenance window scheduled does not.

### Detecting Golden Ticket attacks

The most-cited Kerberos attack, and one that requires AD knowledge to detect:

```
Event ID 4769 (TGS request) appears with:
- Account: any_username (often a non-existent account)
- Service: any_service
- Ticket encryption: RC4 (modern Kerberos uses AES)
- No corresponding Event ID 4768 (TGT request) for this user
```

The forged TGT was created offline using a stolen `krbtgt` hash; the attacker then used it to request a TGS. The KDC has no record of issuing a TGT to this user, and the older RC4 encryption is the giveaway that the ticket was minted by tooling rather than by Microsoft's modern AES-by-default Kerberos implementation.

Without AD/Kerberos knowledge, this pattern is invisible in logs. With it, it's a textbook indicator.

### MITRE ATT&CK mapping

The attacks above all map to specific techniques in the MITRE ATT&CK framework — the standard taxonomy for adversary behaviors that SOC tooling, threat intelligence platforms, and detection engineering teams use to organize their work:

| Technique ID | Name | Relevance |
|--------------|------|-----------|
| **T1558** | Steal or Forge Kerberos Tickets | Golden Ticket, Silver Ticket, Kerberoasting |
| **T1484** | Domain Policy Modification | GPO abuse for persistence or privilege escalation |
| **T1069** | Permission Groups Discovery | Reconnaissance — enumerating Domain Admins, etc. |
| **T1087** | Account Discovery | Reconnaissance — enumerating user accounts |
| **T1550** | Use Alternate Authentication Material | Pass-the-Hash, Pass-the-Ticket, Overpass-the-Hash |

---

## Connection to the lab implementation

The build documents in this repository implement the legitimate side of every mechanism above:

- The directory built in [02 — Domain Controller Setup](02-domain-controller.md) is the same kind of directory attackers enumerate during T1087 (Account Discovery).
- The OUs and groups created in [03 — Identity Structure](03-identity-structure.md) are exactly the targets of T1069 (Permission Groups Discovery).
- The GPOs deployed in [04 — Group Policy](04-group-policy.md) are the substrate that T1484 (Domain Policy Modification) abuses for persistence.
- The PowerShell automation in [05 — PowerShell Automation](05-powershell-automation.md) uses the same `ActiveDirectory` module that attackers use for post-compromise enumeration.

The lab's Phase 3 (planned) extends this directly: configuring the same environment to *generate* authentication-based attack traces (Kerberoasting, Golden Ticket simulations) and correlating them with detection rules in a SIEM. That work depends on having a working domain to attack — which is what the build documents have produced.

---

## Resources

- TryHackMe room: *Active Directory Basics* — primary structured-learning source for the foundational content above
- Microsoft documentation: *Active Directory Domain Services Overview*
- MITRE ATT&CK framework: technique pages for T1558, T1484, T1069, T1087, T1550
- Companion training: *Active Directory Hardening* (TryHackMe) — bridge into Phase 3 work

---

## What this section demonstrates

- **AD theory and SOC operations are inseparable.** Authentication logs only become detection signals when the analyst understands the protocol producing them. Without that understanding, Event IDs 4768 and 4769 are noise; with it, they're attack telemetry.
- **The same mechanisms that enable legitimate operations enable attacks.** Kerberos exists to authenticate users to services. The Golden Ticket attack exists because the same cryptographic primitive can be inverted with a stolen key. The defender's job is not to remove the mechanism but to monitor for inversion.
- **Identity is the highest-leverage domain in security operations.** Network controls fail closed; identity controls fail open. A user who shouldn't have access usually still gets denied; an attacker with valid credentials usually gets through. Investing in identity expertise compounds across most categories of incident.
- **Operational IAM experience and infrastructure-level understanding are complementary, not redundant.** Ten years of executing identity workflows builds intuition for what's normal. Hands-on AD configuration builds intuition for what's possible. The combination is what distinguishes an analyst who can investigate authentication incidents from one who can only escalate them.

