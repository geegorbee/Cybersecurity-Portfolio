Active Directory Home Lab

Enterprise identity infrastructure built from scratch on Windows Server 2022 — domain controller deployment, Group Policy implementation, and PowerShell automation — demonstrating hands-on Active Directory administration for SOC analyst and IT support roles.

Project Status: Phase 1 ✅ Complete · Phase 2 ✅ Complete · Phase 3 🔨 Planned

Overview
This lab provisions a Windows Server 2022 domain controller, joins a Windows 11 client, and implements identity, access, and policy controls representative of a small-enterprise Active Directory environment. The build spans foundational Windows client administration (Microsoft MD-100), domain controller deployment, AD Domain Services and Certificate Services configuration, organizational unit design, Group Policy implementation, file share permission management, and PowerShell-driven user lifecycle automation.
Beyond tutorial completion, the project documents real diagnostic work: the source curriculum (TCM Practical Help Desk) was authored against earlier VirtualBox and Windows Server builds, surfacing installation, virtualization, and network configuration issues that required systematic troubleshooting against current software versions. The troubleshooting log details each issue, root cause analysis, and resolution.

Architecture
#mermaid-rfu{font-family:inherit;font-size:16px;fill:#E5E5E5;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-rfu .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-rfu .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-rfu .error-icon{fill:#CC785C;}#mermaid-rfu .error-text{fill:#3387a3;stroke:#3387a3;}#mermaid-rfu .edge-thickness-normal{stroke-width:1px;}#mermaid-rfu .edge-thickness-thick{stroke-width:3.5px;}#mermaid-rfu .edge-pattern-solid{stroke-dasharray:0;}#mermaid-rfu .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-rfu .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-rfu .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-rfu .marker{fill:#A1A1A1;stroke:#A1A1A1;}#mermaid-rfu .marker.cross{stroke:#A1A1A1;}#mermaid-rfu svg{font-family:inherit;font-size:16px;}#mermaid-rfu p{margin:0;}#mermaid-rfu .label{font-family:inherit;color:#E5E5E5;}#mermaid-rfu .cluster-label text{fill:#3387a3;}#mermaid-rfu .cluster-label span{color:#3387a3;}#mermaid-rfu .cluster-label span p{background-color:transparent;}#mermaid-rfu .label text,#mermaid-rfu span{fill:#E5E5E5;color:#E5E5E5;}#mermaid-rfu .node rect,#mermaid-rfu .node circle,#mermaid-rfu .node ellipse,#mermaid-rfu .node polygon,#mermaid-rfu .node path{fill:transparent;stroke:#A1A1A1;stroke-width:1px;}#mermaid-rfu .rough-node .label text,#mermaid-rfu .node .label text,#mermaid-rfu .image-shape .label,#mermaid-rfu .icon-shape .label{text-anchor:middle;}#mermaid-rfu .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-rfu .rough-node .label,#mermaid-rfu .node .label,#mermaid-rfu .image-shape .label,#mermaid-rfu .icon-shape .label{text-align:center;}#mermaid-rfu .node.clickable{cursor:pointer;}#mermaid-rfu .root .anchor path{fill:#A1A1A1!important;stroke-width:0;stroke:#A1A1A1;}#mermaid-rfu .arrowheadPath{fill:#0b0b0b;}#mermaid-rfu .edgePath .path{stroke:#A1A1A1;stroke-width:2.0px;}#mermaid-rfu .flowchart-link{stroke:#A1A1A1;fill:none;}#mermaid-rfu .edgeLabel{background-color:transparent;text-align:center;}#mermaid-rfu .edgeLabel p{background-color:transparent;}#mermaid-rfu .edgeLabel rect{opacity:0.5;background-color:transparent;fill:transparent;}#mermaid-rfu .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#mermaid-rfu .cluster rect{fill:#CC785C;stroke:hsl(15, 12.3364485981%, 48.0392156863%);stroke-width:1px;}#mermaid-rfu .cluster text{fill:#3387a3;}#mermaid-rfu .cluster span{color:#3387a3;}#mermaid-rfu div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:inherit;font-size:12px;background:#CC785C;border:1px solid hsl(15, 12.3364485981%, 48.0392156863%);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-rfu .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#E5E5E5;}#mermaid-rfu rect.text{fill:none;stroke-width:0;}#mermaid-rfu .icon-shape,#mermaid-rfu .image-shape{background-color:transparent;text-align:center;}#mermaid-rfu .icon-shape p,#mermaid-rfu .image-shape p{background-color:transparent;padding:2px;}#mermaid-rfu .icon-shape rect,#mermaid-rfu .image-shape rect{opacity:0.5;background-color:transparent;fill:transparent;}#mermaid-rfu .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-rfu .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-rfu :root{--mermaid-font-family:inherit;}VirtualBox HostInternal Network: AdLab — 192.168.1.0/24Kerberos · LDAP · SMBNATNATDC01Windows Server 2022192.168.1.10AD DS · AD CS · DNSFile and Storage ServicesWORKSTATION01Windows 11 Pro192.168.1.20Domain-joined clientInternet
Network design rationale: A dual-NIC configuration provides an isolated lab segment (Adapter 1 → Internal Network "AdLab") for all domain traffic, while a separate NAT adapter (Adapter 2) handles internet-bound traffic for OS updates and package installation. This mirrors enterprise practice of segregating administrative network traffic from general egress paths and allows the domain to function deterministically without dependency on host network conditions.

Skills Demonstrated
Hands-On Lab Implementation
Active Directory Administration

Domain controller deployment: forest creation (LAB.local), domain promotion, AD DS configuration
Active Directory Certificate Services (AD CS) installation with SHA-256 root CA private key
DNS configuration for authoritative domain name resolution
Organizational unit hierarchy reflecting business structure (Engineering, IT, Management, Groups)
User and group lifecycle management with assignment to functional OUs
SMB file share creation (EngineeringShare) with NTFS permission scoping and drive mapping

Group Policy Implementation

GPO creation, scoping, and OU linkage in Group Policy Management Console
User Configuration policies: department-specific desktop wallpaper enforcement
Computer Configuration policies: Account Lockout Policy with threshold enforcement
Verification of GPO inheritance and policy application from domain client

PowerShell Automation

RSAT installation and ActiveDirectory module integration
Core cmdlet usage: Get-ADUser, New-ADUser, Set-ADAccountPassword, Set-ADUser
Parameter-driven scripting with Mandatory validation and pipeline-friendly output
Secure credential handling: ConvertTo-SecureString, randomized password generation
End-to-end onboarding automation: Create-ADUser.ps1

Account Recovery Workflow

Configured Account Lockout Policy GPO (3-attempt threshold) at domain root
Reproduced lockout from a domain-joined Windows 11 client
Performed password reset via both GUI (Active Directory Users and Computers) and PowerShell
Forced password change at next logon to enforce credential rotation

Infrastructure Troubleshooting

Diagnosed corrupted Windows Server ISO from interrupted download; resolved by re-downloading in private browsing mode to bypass extension interference
Resolved Windows Server installer I/O failures by switching virtual storage controller from SATA to IDE
Forced GPT disk partitioning via diskpart (clean, convert gpt) to satisfy installer requirements
Identified and resolved AD DS prerequisite conflict caused by premature AD CS role installation
Constructed dual-homed virtual network using VirtualBox Expert Mode following UI reorganization in current releases
Implemented snapshot-based "gold state" backup strategy for repeatable lab restoration

Foundational Knowledge
Microsoft MD-100 Coursework (Phase 1 — completion certificates linked below)

Windows client environment support: Group Policy fundamentals, domain operations, client configuration
Networking on Windows clients: TCP/IP, DNS, DHCP, network troubleshooting
Operating system and application troubleshooting: diagnostic tools, systematic remediation workflows

Active Directory Fundamentals (detailed notes)

Authentication protocols: Kerberos ticket flow (TGT, TGS, KDC) and NetNTLM challenge-response
Security principals: users, machine accounts, groups, and their distinct attack surfaces
Trust relationships: trees, forests, and the asymmetry between trust and access direction
Common authentication-based attack patterns: Golden Ticket, Silver Ticket, Kerberoasting, NTLM Relay
Mapping to MITRE ATT&CK techniques: T1558 (Steal/Forge Kerberos Tickets), T1484 (Domain Policy Modification), T1069 (Permission Groups Discovery), T1087 (Account Discovery)


Repository Navigation
DocumentDescription01 — Lab ArchitectureVM specifications, network topology, design decisions02 — Domain Controller SetupServer 2022 installation, AD DS promotion, AD CS configuration03 — Identity StructureOUs, users, groups, file shares, NTFS permissions04 — Group PolicyGPO creation, linking, verification, lockout policy05 — PowerShell AutomationRSAT, AD cmdlets, Create-ADUser.ps1 walkthrough06 — Troubleshooting LogIssues encountered and resolved during the build07 — Active Directory FundamentalsIdentity, authentication protocols, security context

Documents are published incrementally. Links go live as each section is finalized.


Tools & Technologies
CategoryTechnologyHypervisorOracle VirtualBox 7.x (Expert Mode)Server OSWindows Server 2022 Standard (Evaluation)Client OSWindows 11 ProServer RolesActive Directory Domain Services, Active Directory Certificate Services, DNS Server, File and Storage ServicesAdministrationServer Manager, Active Directory Users and Computers, Group Policy Management ConsoleAutomationPowerShell 5.1 with ActiveDirectory module (RSAT)EditorVisual Studio Code

Project Phases
PhaseScopeStatusPhase 1Windows client administration foundation: client environment support, networking configuration, troubleshooting (Microsoft MD-100)✅ CompletePhase 2Active Directory server administration: domain controller deployment, OU and user provisioning, file shares, Group Policy, PowerShell automation, account lockout and recovery✅ CompletePhase 3Security hardening and detection: tiered administrative model, GPO security baselines, attack simulation (Kerberoasting, Golden Ticket), authentication log correlation in SIEM🔨 Planned
Phase 1 Microsoft Learn completion certificates

Monitor and troubleshoot Windows client performance
Employ remote management
Troubleshoot operating system service issues


About This Project
This lab is part of a structured progression toward Security Operations Center (SOC) analyst and IT support roles, with focus on the identity domain — the area most commonly leveraged in authentication-based attacks, lateral movement, and privilege escalation. Phase 3 will extend the environment with security hardening and threat detection scenarios that build on the infrastructure documented here.
Last updated: May 2026
