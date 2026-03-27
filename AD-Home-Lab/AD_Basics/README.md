# Active Directory Fundamentals - Enterprise Identity Infrastructure

## Overview

I completed comprehensive hands-on training in Active Directory (AD), the backbone of enterprise identity and access management used by virtually every Windows-based organization worldwide. This training provided practical experience configuring domain controllers, managing users and computers, implementing Group Policy security controls, and understanding authentication protocols - all core components of the Identity domain where I have 10+ years operational experience.

While my federal government role provided deep operational knowledge of identity lifecycle management, authentication workflows, and access control enforcement, this training formalized my understanding of the underlying Active Directory infrastructure that powers those operations. This combination of hands-on technical AD configuration experience and extensive real-world IAM operations positions me to bridge the gap between identity administration and identity security - a critical capability for SOC analysts investigating authentication-based attacks and lateral movement.

**Note:** This Active Directory foundation integrates with my ongoing AD Home Lab project where I'm implementing enterprise security controls including tiered administrative models, Group Policy hardening, and identity threat detection scenarios.

---

## Learning Objectives

Through this hands-on lab, I developed capabilities in:

**Active Directory Architecture:**
- Understanding Windows domains and Domain Controller roles
- Distinguishing between users, groups, machines, and organizational units
- Designing OU structures that mirror business organization
- Managing security principals and authentication workflows

**Identity Management Operations:**
- Creating and managing user accounts across departments
- Implementing security groups for access control
- Delegating administrative privileges following least-privilege principles
- Organizing computer objects (workstations, servers, domain controllers)

**Group Policy Implementation:**
- Creating Group Policy Objects (GPOs) for security baseline enforcement
- Linking GPOs to organizational units for targeted policy deployment
- Configuring computer and user policies independently
- Understanding GPO inheritance and security filtering

**Authentication Protocols:**
- Deep-dive into Kerberos ticket-based authentication (TGT, TGS, KDC)
- Understanding NetNTLM challenge-response mechanism
- Recognizing authentication security implications
- Identifying opportunities for credential theft and attack

**Enterprise Architecture:**
- Designing multi-domain environments using trees and forests
- Implementing trust relationships for cross-domain resource access
- Distinguishing Domain Admins from Enterprise Admins
- Planning scalable identity infrastructure for growing organizations

---

## Active Directory Core Components

### Security Principals: Users, Groups, and Machines

Active Directory manages three primary types of security principals - objects that can be authenticated and granted privileges:

**Users:**

Security principals representing:
- **People:** Employees requiring network access for daily work
- **Services:** Service accounts for IIS, MSSQL, applications (limited privileges)

Users are the most common AD object and the primary target for authentication-based attacks. Understanding user lifecycle (creation → modification → disablement → deletion) is critical for both administration and security operations.

**Connection to My Experience:**
My 10 years managing identity operations involved daily user lifecycle management across 100+ accounts. This training formalized the underlying AD mechanisms I've been executing operationally.

**Machines:**

Every computer joining an AD domain receives a machine account:
- Machine accounts are security principals with domain authentication capability
- Named with computer name + dollar sign (e.g., `DC01$`, `WORKSTATION05$`)
- Passwords automatically rotate (120 random characters)
- Local administrators on assigned computers only

**Security Implications:**
Machine accounts are often overlooked in security operations, but compromising a machine account enables:
- Pass-the-hash attacks using machine credentials
- Lateral movement to systems where machine has local admin
- Kerberos silver ticket attacks if service password known

**Groups:**

Collections of users and/or machines for access control:
- Enable bulk permission assignment (file shares, printers, applications)
- Can contain users, machines, and nested groups
- Also security principals (groups can be granted privileges)

**Critical Default Groups:**

| Group | Privilege Scope |
|-------|----------------|
| **Domain Admins** | Full domain control including all computers and DCs |
| **Enterprise Admins** | Administrative control across entire forest |
| **Server Operators** | Can administer DCs but not modify admin groups |
| **Backup Operators** | Access any file (ignoring permissions) for backup |
| **Account Operators** | Create/modify user accounts in domain |
| **Domain Users** | All users in domain (default membership) |
| **Domain Computers** | All computers in domain |

**Attack Surface Awareness:**
- Domain Admins and Enterprise Admins are primary targets (credential theft = domain compromise)
- Backup Operators can access any file - valuable for data exfiltration
- Account Operators can create backdoor accounts for persistence

### Organizational Units (OUs)

Container objects that organize AD for policy deployment:

**OU Structure Design:**

Best practice mirrors business organization:
```
Domain: thm.local
├── Domain Controllers (default)
├── Computers (default - to be reorganized)
├── Users (default - legacy)
├── Workstations (custom - user PCs)
├── Servers (custom - infrastructure)
└── Departments (custom OU structure):
    ├── IT
    ├── Management
    ├── Marketing
    ├── Sales
    └── R&D
```

**Key OU Principles:**
- Users can only belong to ONE OU (no dual membership)
- OUs enable targeted Group Policy deployment
- Child OUs inherit parent OU policies (unless blocked)
- Used for administrative delegation (department-level admin rights)

**OUs vs Security Groups - Critical Distinction:**

| Organizational Units | Security Groups |
|---------------------|-----------------|
| Apply policies (GPOs) | Grant resource access |
| User in ONE OU only | User in MANY groups |
| Hierarchy-based | Membership-based |
| For configuration management | For permission management |

**Real-World Example from My Experience:**
In federal operations, we had department-based OUs (similar to this lab) where authentication policies, password requirements, and MFA enforcement varied by organizational sensitivity. IT staff had stricter requirements than general users. This OU-based policy model enabled risk-appropriate security controls.

---

## Practical Identity Administration

### User Lifecycle Management

**Hands-On Exercise: Organizational Restructuring**

Scenario: Business reorganization requires AD changes to match new org chart:
- Department closure (remove entire OU and contained users)
- New employees hired (create user accounts in department OUs)
- Employees transferred (move between OUs or delete/recreate)

**Deletion Protection:**
By default, OUs have accidental deletion protection enabled. To delete:
1. Enable "Advanced Features" in View menu
2. Right-click OU → Properties → Object tab
3. Uncheck "Protect object from accidental deletion"
4. Confirm deletion (cascades to all child objects)

**Security Consideration:**
Deleted user accounts should be documented as part of offboarding procedures. Attackers may create accounts with names similar to recently deleted users to evade detection ("John.Smith" deleted, "JSmith" created by attacker).

### Administrative Delegation

**Principle of Least Privilege Implementation:**

Rather than granting Domain Admin rights to helpdesk staff, delegate specific privileges:

**Example: Password Reset Delegation**

Scenario: Phillip (IT Support) needs password reset capability for Sales, Marketing, and Management departments, but NOT full domain admin rights.

**Delegation Process:**
1. Right-click target OU (e.g., Sales) → Delegate Control
2. Select user: `phillip`
3. Choose task: "Reset user passwords and force password change at next logon"
4. Apply to OU

**Result:** Phillip can reset passwords within delegated OUs using PowerShell:

```powershell
# Reset password for user Sophie
Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose

# Force password change at next logon
Set-ADUser -ChangePasswordAtLogon $true -Identity sophie -Verbose
```

**Security Value:**
- Reduces Domain Admin account usage (smaller attack surface)
- Limits blast radius if delegated account compromised
- Enables audit trail of who reset which passwords
- Implements separation of duties

**Connection to My Experience:**
This is exactly how we operated in federal environment - Team Leads had delegated password reset authority within their organizational boundaries, but not domain-wide admin rights. This training formalized the AD mechanism behind those delegated privileges.

---

## Group Policy Security Implementation

### Group Policy Objects (GPOs)

**What GPOs Provide:**

Centralized configuration management across domain:
- Security baselines (password policies, account lockout)
- Desktop restrictions (Control Panel access, USB blocking)
- Software deployment and configuration
- Audit policy enforcement
- Startup/shutdown scripts

**GPO Structure:**

Each GPO contains two sections:
- **Computer Configuration:** Applies to machines (regardless of logged-in user)
- **User Configuration:** Applies to users (regardless of which machine they use)

**GPO Application Workflow:**

1. Create GPO under "Group Policy Objects"
2. Configure settings in GPO Editor
3. Link GPO to target OU(s)
4. GPO propagates via SYSVOL share on Domain Controllers
5. Clients sync GPOs periodically (max 2 hours) or via `gpupdate /force`

### Hands-On GPO Implementation

**Scenario 1: Restrict Control Panel Access**

**Business Requirement:** Only IT department should access Control Panel on domain computers. Sales, Marketing, and Management users should be restricted.

**GPO Configuration:**
- GPO Name: `Restrict Control Panel Access`
- Setting: `User Configuration → Policies → Administrative Templates → Control Panel`
- Policy: "Prohibit access to Control Panel and PC settings" = **Enabled**
- Linked to: Sales OU, Marketing OU, Management OU (NOT linked to IT OU)

**Result:** Users in linked OUs receive "This operation has been cancelled due to restrictions in effect" when attempting Control Panel access.

**Security Rationale:**
- Prevents non-IT users from modifying system settings
- Reduces risk of misconfiguration or security control bypass
- Enforces separation of duties (system configuration = IT only)

**Scenario 2: Automatic Screen Lock**

**Business Requirement:** Workstations and servers must auto-lock after 5 minutes inactivity to prevent session hijacking.

**GPO Configuration:**
- GPO Name: `Auto Lock Screen`
- Setting: `Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → Security Options`
- Policy: "Interactive logon: Machine inactivity limit" = **300 seconds**
- Linked to: Root domain (`thm.local`) for inheritance across all child OUs

**Design Decision:**
Link to root domain rather than individual OUs because:
- Applies to ALL computers universally (consistent security baseline)
- OUs containing only users ignore Computer Configuration (no wasted processing)
- Simpler management (one GPO vs. multiple duplicate GPOs)

**Security Value:**
- Mitigates "clean desk" policy violations (users leaving sessions active)
- Prevents unauthorized access to unattended workstations
- Compliance requirement for many regulatory frameworks (PCI-DSS, HIPAA)

### GPO Security Filtering

**Advanced Targeting:**

Beyond OU-based GPO application, security filtering enables:
- Apply GPO only to specific security groups
- Exclude specific users/computers from OU-linked GPO
- Combine OU structure with group membership for fine-grained control

**Default:** GPOs apply to "Authenticated Users" (everyone in linked OU)

**Use Case Example:**
- Link GPO to entire IT OU
- Security filter to exclude "Domain Admins" group
- Result: IT staff affected except Domain Admins

---

## Authentication Protocols Deep Dive

### Kerberos: Ticket-Based Authentication

**Why Kerberos Matters for Security Operations:**

Understanding Kerberos is critical for:
- Detecting credential theft attacks (Golden Ticket, Silver Ticket)
- Investigating lateral movement (pass-the-ticket attacks)
- Analyzing authentication logs in SIEM platforms
- Identifying Kerberoasting (service account password cracking)

**Kerberos Authentication Flow:**

**Phase 1: TGT Request (Initial Authentication)**

```
User → Key Distribution Center (KDC):
- Username + Timestamp (encrypted with user's password-derived key)

KDC → User:
- Ticket Granting Ticket (TGT) - encrypted with krbtgt account hash
- Session Key (for future requests)
```

**Key Points:**
- TGT proves user authenticated without re-sending password
- TGT encrypted by `krbtgt` account (DC service account)
- Compromising `krbtgt` hash = Golden Ticket attack (forged TGTs)
- Session Key known to user and KDC (embedded in encrypted TGT)

**Phase 2: TGS Request (Service Access)**

```
User → KDC:
- TGT (proving prior authentication)
- Service Principal Name (SPN) - target service identifier
- Timestamp encrypted with Session Key

KDC → User:
- Ticket Granting Service (TGS) - encrypted with service owner's hash
- Service Session Key (for authenticating to service)
```

**Key Points:**
- TGS grants access to ONE specific service only
- TGS encrypted with service account's password hash
- Service Session Key proves legitimate TGS possession
- Each service requires separate TGS

**Phase 3: Service Authentication**

```
User → Service:
- TGS (encrypted with service account hash)
- Authenticator (encrypted with Service Session Key)

Service:
- Decrypts TGS using its own password hash
- Extracts Service Session Key
- Validates authenticator
- Grants access if valid
```

**Attack Surface Analysis:**

| Attack | Target | Impact |
|--------|--------|--------|
| **Golden Ticket** | `krbtgt` hash | Forge TGTs for any user (domain persistence) |
| **Silver Ticket** | Service account hash | Forge TGS for specific service (stealth access) |
| **Kerberoasting** | Service accounts | Crack weak service account passwords offline |
| **Pass-the-Ticket** | Stolen TGT/TGS | Reuse valid tickets (no password needed) |
| **Overpass-the-Hash** | User NTLM hash | Request TGT using hash instead of password |

**Connection to My Splunk Investigation:**

In my "Investigating with Splunk" project, I analyzed Windows Security Event IDs 4768 (TGT request) and 4769 (TGS request) to detect lateral movement. Understanding the Kerberos flow behind those events enables accurate threat detection vs. false positive determination.

### NetNTLM: Legacy Challenge-Response

**NetNTLM Authentication Flow:**

```
1. Client → Server: Authentication request
2. Server → Client: Random challenge value
3. Client: Combines NTLM hash + challenge = response
4. Client → Server: Challenge response
5. Server → Domain Controller: Challenge + Response for validation
6. DC: Recalculates expected response, compares with received
7. DC → Server: Authentication result (success/failure)
8. Server → Client: Access granted/denied
```

**Critical Security Implication:**

Password/hash NEVER transmitted over network, BUT:
- NetNTLM susceptible to relay attacks (pass challenge/response to another service)
- Weaker than Kerberos (no mutual authentication)
- Legacy protocol kept for backward compatibility only

**Attack: NTLM Relay**

Attacker intercepts challenge-response and replays to different service:
1. Victim connects to attacker-controlled service
2. Attacker relays challenge from legitimate service to victim
3. Victim calculates response (thinking they're authenticating to attacker)
4. Attacker forwards victim's response to legitimate service
5. Legitimate service accepts (valid response to its challenge)
6. Attacker gains access using victim's privileges

**Mitigation:** SMB signing, LDAP signing, EPA (Extended Protection for Authentication)

---

## Enterprise Architecture: Trees, Forests, and Trusts

### Scaling Beyond Single Domain

**When to Use Multiple Domains:**

Reasons for domain splitting:
- **Geographic distribution:** Different countries with different regulations/policies
- **Organizational autonomy:** Acquired companies maintaining separate IT infrastructure
- **Administrative delegation:** Completely separate IT teams managing different business units
- **Security isolation:** Highly sensitive environments requiring hard boundaries

### Trees: Shared Namespace Hierarchy

**Example: Geographic Expansion**

```
Root Domain: thm.local (corporate headquarters)
├── uk.thm.local (United Kingdom operations)
├── us.thm.local (United States operations)
└── asia.thm.local (Asia-Pacific operations)
```

**Tree Characteristics:**
- Shared namespace (all domains end in `.thm.local`)
- Automatic two-way trust relationships between parent-child domains
- Each domain has its own Domain Controllers
- Each domain has its own Domain Admins (domain-specific control)
- Enterprise Admins have control across entire tree

**Administrative Model:**

| Role | Scope |
|------|-------|
| **Domain Admins (UK)** | Full control over `uk.thm.local` only |
| **Domain Admins (US)** | Full control over `us.thm.local` only |
| **Enterprise Admins** | Full control across all domains in tree |

**Use Case:**
UK IT team manages UK users/computers without ability to accidentally (or maliciously) affect US operations. Policies can differ (GDPR compliance in UK vs. other regulations in US).

### Forests: Multiple Namespaces

**Example: Company Merger**

```
Forest (merged organization):
├── Tree 1: thm.local
│   ├── uk.thm.local
│   └── us.thm.local
└── Tree 2: mht.local (acquired company)
    ├── eu.mht.local
    └── asia.mht.local
```

**Forest Characteristics:**
- Multiple independent namespaces (`thm.local` and `mht.local`)
- Separate domain trees managed independently
- Trust relationships enable resource sharing across trees
- Each tree maintains its own Enterprise Admins

**Business Scenario:**
THM Inc. acquires MHT Inc. Both companies maintain separate IT infrastructure but need occasional resource sharing (file servers, applications). Forest trust enables UK user at `thm.local` to access file server in `mht.local` with proper authorization.

### Trust Relationships

**Trust Direction vs. Access Direction:**

CRITICAL CONCEPT: Trust direction is OPPOSITE of access direction.

**One-Way Trust:**
```
Domain A ----trusts----> Domain B

Meaning: 
- Domain A trusts Domain B's authentication
- Users in Domain B can be authorized in Domain A
- Users in Domain A CANNOT access Domain B resources
```

**Visual: "Trust flows backward, access flows forward"**

**Two-Way Trust:**
```
Domain A <----trusts----> Domain B

Meaning:
- Both domains trust each other's authentication
- Users in both domains can be authorized in either domain
- Default configuration for trees and forests
```

**Trust Does NOT Equal Access:**

IMPORTANT: Trust enables authorization possibility, but doesn't grant access automatically.

**Example:**
- UK domain trusts US domain
- US user `john.smith` can be AUTHORIZED on UK file server
- But UK admin must explicitly grant `US\john.smith` file permissions
- Trust provides authentication mechanism only

### Security Implications of Trusts

**Attack Surface Expansion:**

Trusts create lateral movement opportunities:
- Compromise low-privilege account in trusted domain
- Enumerate trust relationships
- Exploit weak permissions in trusting domain
- Escalate privileges across domain boundary

**Domain Trust Attacks:**
- **SID History injection:** Add privileged SID to user crossing trust
- **Foreign Security Principals:** Enumerate cross-domain group memberships
- **Trust key compromise:** Forge inter-domain TGTs if trust key stolen

**Defense:**
- Implement Selective Authentication on trusts (not automatic access)
- Monitor cross-domain authentication events (Event ID 4769 with trust TGS)
- Limit Domain Admin privileges to single domain (use separate accounts across domains)

---

## Integration with Security Operations

### Connecting AD Knowledge to SOC Investigations

**Scenario 1: Detecting Lateral Movement**

**Splunk Alert:** Multiple authentication attempts from single source to multiple destinations on port 445 (SMB).

**Investigation Workflow with AD Knowledge:**

1. **Identify source account type:**
   - User account? (potential credential theft)
   - Machine account? (could be legitimate or compromised workstation)

2. **Check account privileges:**
   - Member of Domain Admins? (high-value target confirmation)
   - Service account? (possible Kerberoasting victim)

3. **Analyze authentication protocol:**
   - Kerberos (Event ID 4768, 4769): Check for suspicious SPNs
   - NTLM (Event ID 4776): Possible NTLM relay attack

4. **Review Group Policy application:**
   - Should this user access these systems? (GPO violations)
   - Workstation restriction policies in place? (policy bypass attempt)

**AD-Informed Detection:**
Without AD knowledge: "Multiple SMB connections = maybe suspicious?"
With AD knowledge: "Service account authenticating to workstations after hours using NTLM = probable credential theft + relay attack"

**Scenario 2: Privilege Escalation Detection**

**SIEM Alert:** User account added to privileged group.

**Investigation with AD Context:**

1. **Which group?**
   - Domain Admins = critical (full domain control)
   - Account Operators = concerning (can create backdoor accounts)
   - Backup Operators = worrying (can access any file)

2. **Who made the change?**
   - Domain Admin account? (verify legitimate action)
   - Regular user account? (impossible - escalation vulnerability)
   - Machine account? (very suspicious - malware/exploit)

3. **From which system?**
   - Domain Controller? (administrative console = expected)
   - Workstation? (remote admin tools = verify legitimacy)
   - Non-domain system? (external attack vector)

4. **Time and context:**
   - During business hours? (more likely legitimate)
   - 3 AM on Sunday? (suspicious - compromised admin account?)

**Scenario 3: Golden Ticket Detection**

**Indicators requiring AD authentication knowledge:**

```
Event ID 4769 (TGS Request) with:
- Account: any_username
- Service: any_service
- Ticket encryption: RC4 (unusual - modern Kerberos uses AES)
- Source: does not match prior TGT Event ID 4768 for this user
```

**Why this indicates Golden Ticket:**
- Attacker forged TGT using stolen `krbtgt` hash
- Forged ticket used to request TGS
- No prior authentic TGT request (attacker bypassed KDC authentication)
- Older encryption type (attacker using simple hash, not full Kerberos)

**Without AD/Kerberos knowledge:** Undetectable in logs.
**With AD/Kerberos knowledge:** Clear attack pattern.

### MISP Integration: AD-Specific IOCs

From my MISP training, AD-related indicators to share:

**Network Indicators:**
- IP addresses of rogue Domain Controllers
- C2 infrastructure using port 88 (Kerberos) or 389 (LDAP) for blending

**Account Indicators:**
- Compromised service account names (Kerberoasting targets)
- Backdoor account naming patterns (SVC_admin, backup_user)

**Behavioral Indicators:**
- Unusual SPN values (malicious Kerberos delegation)
- Suspicious Group Policy modifications (persistence via GPO)

**MITRE ATT&CK Mapping:**
AD-specific techniques from my MITRE framework training:
- T1558 (Steal or Forge Kerberos Tickets)
- T1484 (Domain Policy Modification - GPO abuse)
- T1069 (Permission Groups Discovery - recon)
- T1087 (Account Discovery - enumeration)

---

## Connection to Active Directory Home Lab

**This TryHackMe training provides foundation for my ongoing AD Home Lab project:**

**Phase 1 - Basic Implementation (MD-100 Certified):**
- Domain Controller deployment ✅
- OU structure design ✅
- User/computer object management ✅
- Group Policy basics ✅

**Phase 2 - Security Hardening (In Progress):**
- Tiered administrative model implementation
- Privileged Access Workstation (PAW) configuration
- Advanced GPO security baselines
- Audit policy for threat detection

**Phase 3 - Attack & Defense Scenarios (Planned):**
- Kerberoasting attack simulation and detection
- Golden/Silver ticket attacks with SIEM correlation
- NTLM relay attacks and mitigation verification
- Lateral movement detection via authentication log analysis

**Integration with Other Projects:**

**With Splunk Analysis:**
- AD generates authentication events (4624, 4625, 4768, 4769)
- Splunk ingests and correlates AD logs
- Detection rules leverage AD architecture knowledge

**With Wireshark:**
- Capture Kerberos traffic (port 88) for protocol analysis
- Analyze LDAP queries (port 389) for enumeration detection
- Inspect SMB authentication (NTLM vs. Kerberos)

**With MITRE/MISP:**
- Map observed AD attacks to ATT&CK techniques
- Share compromised account IOCs via MISP
- Document GPO-based persistence in threat intelligence

---

## Key Takeaways

**Technical Skills Developed:**
- Active Directory architecture and component relationships
- Identity lifecycle management (users, groups, machines)
- Group Policy creation, linking, and troubleshooting
- Kerberos and NetNTLM authentication protocol internals
- Enterprise AD design (trees, forests, trusts)
- Administrative delegation and least-privilege implementation

**Security Operations Capabilities:**
- Recognizing authentication-based attacks through AD knowledge
- Detecting privilege escalation via group membership monitoring
- Investigating lateral movement using Kerberos ticket analysis
- Identifying policy violations through GPO enforcement awareness
- Understanding trust relationship attack surface

**Operational Understanding:**
- Why AD is the "backbone of corporate networks"
- How centralized identity management scales across enterprise
- Balance between administrative convenience and security isolation
- Importance of OU structure for policy deployment
- Critical role of Domain Controllers in security architecture

---

## Connection to Identity Specialization

**10 Years IAM Operations + AD Technical Foundation = Identity Security Expertise**

**My Career Positioning:**

**Before this training:**
- Deep operational knowledge of identity workflows
- Extensive authentication troubleshooting experience
- Access control enforcement across 100+ users
- But: Operational perspective without underlying AD technical depth

**After this training:**
- Formalized AD architecture and component understanding
- Protocol-level authentication knowledge (Kerberos internals)
- Group Policy security implementation capability
- Attack surface awareness from attacker perspective

**Result:** Can bridge identity administration and identity security - understanding both legitimate operations AND how attackers abuse those same mechanisms.

**For SOC Analyst Roles:**

This positions me to:
- Investigate authentication-based attacks with deep context
- Distinguish legitimate AD operations from malicious activity
- Correlate authentication logs with AD infrastructure knowledge
- Communicate findings using accurate AD terminology
- Recommend remediation aligned with AD security best practices

**For Identity-Focused Security Roles:**

Demonstrates capability for:
- IAM security architecture review
- Privileged access management implementation
- Authentication protocol security assessment
- AD hardening and security baseline development

---

## Resources

- **TryHackMe Room:** Active Directory Basics
- **Microsoft Documentation:** Active Directory Domain Services Overview
- **MITRE ATT&CK:** Active Directory specific techniques
- **Related Training:** Active Directory Hardening (TryHackMe)
- **Advanced Learning:** Compromising Active Directory module (TryHackMe)

---

## Status: FOUNDATION COMPLETE ✅

**Integration with AD Home Lab Project:** In Progress

**Next Steps:**
- Complete AD Hardening room (security baselines)
- Implement tiered administration model in home lab
- Document attack scenarios (Kerberoasting, Golden Ticket)
- Correlate AD events with Splunk SIEM for detection

This Active Directory foundation demonstrates enterprise identity infrastructure knowledge - essential capability for SOC analysts investigating authentication-based attacks, lateral movement, and privilege escalation in Windows environments. Combined with 10 years operational IAM experience, this positions me as an Identity domain specialist for security operations roles.

