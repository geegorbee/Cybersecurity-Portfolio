# Troubleshooting Log

The TCM Practical Help Desk course this lab follows was authored against earlier releases of VirtualBox and Windows Server. Working through it on current software surfaced a series of issues where the documented steps no longer produced the expected result. This log captures each one — what was observed, what was actually wrong underneath, and what resolved it.

The point of capturing this isn't to complain about an outdated course. It's that real systems work looks more like this than like a clean tutorial run, and being able to identify, isolate, and fix issues across multiple layers (download, hypervisor, OS installer, role dependencies) is closer to the actual job than smoothly executing a script.

---

## Issue 1 — Corrupted installation media

**Symptom.** During Windows Server 2022 installation, the installer halted with the error: *"Windows cannot find the Microsoft Software License Terms."*

**Diagnosis.** The error suggests a file inside the install image is missing or unreadable. Re-running the installer produced the same result, which ruled out a transient hiccup. The original Server 2022 ISO had been downloaded from the Microsoft Evaluation Center over a connection that briefly dropped during the transfer — likely truncating the file without flagging an obvious size mismatch on disk.

**Resolution.** Re-downloaded the ISO from a private/incognito browser session to bypass any browser extensions (download managers, ad blockers) that might have interfered with stream integrity. Verified the new download was complete before mounting. Installation proceeded normally.

**Takeaway.** Installer error messages often describe the symptom (missing file) rather than the cause (corrupt source). When the same error reproduces deterministically, suspect the input artifact before assuming installer or hardware fault.

---

## Issue 2 — Installer failing to read from virtual disk

**Symptom.** Even with a verified-clean ISO, the Server 2022 installer threw inconsistent read errors during the file-copy phase. Errors included variations of license-file failures (similar to Issue 1, but now with a known-good ISO) and generic "cannot read installation source" messages.

**Diagnosis.** The same ISO worked correctly when tested in a different VM configuration, which pointed at the virtual storage controller rather than the media. VirtualBox defaults to attaching ISOs through a SATA controller, and on this host that combination produced the unreliable I/O. Modern Server installers are more sensitive to controller behavior than the older tutorial assumed.

**Resolution.** In VirtualBox VM settings → Storage, removed the ISO from the SATA controller and reattached it to an IDE controller. Installation completed without further read errors.

**Takeaway.** When error messages from a higher layer (installer) look random, drop a layer down (storage controller). Virtual hardware choice is a real configuration variable, not a default to leave untouched.

---

## Issue 3 — Installer not recognizing the virtual disk layout

**Symptom.** With the storage controller fix in place, the installer proceeded further but did not present the expected partition layout for the target virtual disk. Selecting the disk produced format-related warnings rather than a clean installable target.

**Resolution.** From the installer's command-prompt fallback (Shift+F10), used `diskpart` to force a known-good disk state:

```cmd
diskpart
list disk
select disk 0
clean
convert gpt
exit
```

The `clean` command zeroed the partition table; `convert gpt` set the disk to GUID Partition Table format, which the modern UEFI-based installer expects. The installer then recognized the disk normally.

**Takeaway.** `diskpart` is one of those tools that's invisible until you need it, then indispensable. Knowing it exists and how to drop into it from the installer environment is the difference between starting over and finishing the install.

---

## Issue 4 — AD DS promotion blocked by premature AD CS install

**Symptom.** During the Active Directory Domain Services post-install configuration (the step that promotes a server to a domain controller), the prerequisite check failed and refused to continue.

**Diagnosis.** Reviewing the prerequisite report showed the conflict came from Active Directory Certificate Services, which had been installed earlier in the build. AD CS expects to be configured *after* the server is already a domain controller, because in production it depends on directory services for certificate template publishing. Installing it first creates a chicken-and-egg state the installer won't resolve automatically.

**Resolution.** Removed the AD CS role via Server Manager → Remove Roles and Features. Restarted, then re-ran the AD DS promotion, which completed cleanly. After the server was promoted to a domain controller, re-installed AD CS — at which point its dependency on directory services was satisfied and configuration succeeded.

**Takeaway.** Role install order is a dependency tree, not a checklist. Reading prerequisite errors literally — "what role does this one need first?" — is faster than retrying the same install and hoping for a different result.

---

## Issue 5 — VirtualBox network configuration after UI redesign

**Symptom.** The course's network setup steps referenced UI elements that no longer existed in current VirtualBox releases. Specifically, the path to configure Internal Network names and per-adapter detail had been reorganized into a more compact basic view, with advanced controls hidden.

**Resolution.** Switched VirtualBox VM settings to **Expert Mode** (toggle at the top of the Settings dialog), which exposes all four adapter slots and the full set of attachment options simultaneously. Built the dual-NIC topology by hand:

| Adapter | Attached to | Purpose |
|---------|-------------|---------|
| Adapter 1 | Internal Network → name `AdLab` | Isolated lab segment for domain traffic |
| Adapter 2 | NAT | Internet egress for OS updates |

Within the guest, statically assigned IPs (`192.168.1.10` for the DC, `192.168.1.20` for the client) on the AdLab adapter, with DNS pointing to the DC's address (`192.168.1.10`) so the domain-joined client could resolve the domain authoritatively.

**Takeaway.** When tutorial UI references go stale, the underlying capability usually hasn't changed — just the path to it. Expert Mode in VirtualBox surfaces the controls older guides assume are visible by default.

> **Screenshots:** see [`images/06-troubleshooting/adapter1-internal.png`](../images/06-troubleshooting/adapter1-internal.png) and [`images/06-troubleshooting/adapter2-nat.png`](../images/06-troubleshooting/adapter2-nat.png) for the dual-NIC configuration in Expert Mode.

---

## Issue 6 — Password reset blocked by account flag

**Symptom.** While testing the account lockout / recovery workflow, attempted to reset a locked-out user's password through Active Directory Users and Computers. The reset dialog presented but the change did not take effect as expected — the account stayed in a state where the temporary password could not be applied cleanly.

**Diagnosis.** Earlier in the build, when creating the test user accounts, the **Password never expires** flag had been set on the user object's account properties. This flag interacts with the *User must change password at next logon* option in a way that blocks the standard lockout-recovery flow, where the admin sets a temporary password and forces the user to rotate it on next login.

**Resolution.** Opened the user's account properties, unchecked **Password never expires**, then re-issued the password reset with **User must change password at next logon** enabled. The user could then log in with the temporary credential and was correctly prompted to set their own password.

**Takeaway.** Account flags aren't independent toggles; some of them have implicit interactions. *Password never expires* is convenient for service accounts but it isn't a "set and forget" choice for human users — it changes how other recovery mechanisms behave.

---

## Snapshot strategy

Each of the issues above was easier to recover from because of a deliberate snapshot regimen taken at known-good states:

1. **Post-OS install** — clean Server 2022, before any role configuration
2. **Post-static IP configuration** — networking confirmed working before introducing AD complexity
3. **Pre-AD DS promotion** — last point at which the server is still a member, not a controller

When Issue 4 (the AD CS / AD DS conflict) hit, the path back to a clean state was minutes rather than a full reinstall. Snapshot discipline is cheap insurance and is the closest a home lab gets to the change-management practices that production environments enforce formally.

---

## What this section is meant to demonstrate

- **Layered diagnosis.** Issues at the installer level were caused by problems at the storage controller, partition table, and source-media levels. Identifying which layer to look at is more useful than memorizing fixes.
- **Reading errors literally.** The license-file error in Issue 1 *was* describing a missing file — the cause was upstream. Prerequisite errors in Issue 4 *did* tell you which dependency was wrong — they had to be read, not skimmed.
- **Working with current tooling against older instructions.** UI changes, default behavior changes, and modernized installer assumptions are normal facts of life. Translating older steps into current equivalents is part of the skill, not a flaw in execution.
- **Documenting as you go.** Each entry above was captured at the time the issue was resolved, not reconstructed afterward. This habit transfers directly to the case-note discipline that SOC and IT support roles depend on.
