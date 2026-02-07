# Splunk Detection & Analysis Portfolio

## Overview
Hands-on Splunk SIEM experience through TryHackMe's structured learning path, demonstrating log analysis, threat detection, and investigation capabilities. This portfolio showcases practical security analyst skills including event correlation, threat hunting, incident investigation, and detection rule development.

## Skills Demonstrated
- **SPL (Search Processing Language)** query development and optimization
- **Security event correlation** across multiple Windows log sources
- **Threat hunting** using MITRE ATT&CK framework
- **Incident investigation** methodology and documentation
- **Windows Event ID** interpretation (Security, Sysmon, PowerShell)
- **Detection rule** development for common attack patterns
- **SIEM dashboard** creation for security monitoring

---

## Completed Labs

### 1. Splunk: The Basics
**Repository:** [THM-Splunk-Basics](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/Splunk-Detection-Analysis/THM-Splunk-Basics)

**Skills Covered:**
- Splunk interface navigation and search fundamentals
- Basic SPL syntax and field extraction
- Time range filtering and search optimization
- Index and sourcetype usage

---

### 2. Splunk: Exploring SPL
**Repository:** [THM-SPL-Exploration](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/Splunk-Detection-Analysis/THM-SPL-Exploration)

**Skills Covered:**
- Advanced SPL commands (`stats`, `eval`, `table`, `sort`)
- Statistical analysis and data aggregation
- Field manipulation and calculated fields
- Search pipeline optimization

---

### 3. Investigating with Splunk
**Repository:** [THM-Investigating-with-Splunk](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/Splunk-Detection-Analysis/THM-Investigating-with-Splunk)

**Skills Covered:**
- Real-world SOC investigation workflow
- Multi-host threat hunting across Windows environments
- MITRE ATT&CK framework mapping
- Backdoor detection and persistence mechanism analysis
- PowerShell script decoding and malware analysis
- Evidence correlation and timeline reconstruction

**Key Investigation Highlights:**
- Identified backdoor user creation via Windows Event ID 4720
- Traced registry persistence mechanisms using Sysmon telemetry
- Decoded obfuscated PowerShell C2 communications
- Mapped adversary TTPs to MITRE ATT&CK techniques
- Documented detection gaps and recommended improvements

---

## Sample Detection Rules

### 1. Brute Force Authentication Detection
```spl
index=main EventCode=4625 
| stats count by src_ip, Account_Name 
| where count > 5
| eval risk_score=case(count>20, "Critical", count>10, "High", count>5, "Medium")
| table src_ip, Account_Name, count, risk_score
```
**Purpose:** Detect multiple failed login attempts indicating brute force activity  
**MITRE ATT&CK:** T1110 - Brute Force

---

### 2. Privilege Escalation Monitoring
```spl
index=main (EventCode=4672 OR EventCode=4720 OR EventCode=4728)
| eval event_description=case(
    EventCode=4672, "Special privileges assigned",
    EventCode=4720, "User account created", 
    EventCode=4728, "Member added to security-enabled group")
| table _time, host, Account_Name, event_description
| sort - _time
```
**Purpose:** Monitor for privilege escalation indicators  
**MITRE ATT&CK:** T1078 - Valid Accounts, T1136 - Create Account

---

### 3. After-Hours Access Alerts
```spl
index=main EventCode=4624 Logon_Type=10
| eval hour=strftime(_time, "%H")
| where hour < 6 OR hour > 22
| table _time, host, Account_Name, src_ip, hour
| sort - _time
```
**Purpose:** Detect unusual access patterns outside business hours  
**MITRE ATT&CK:** T1078 - Valid Accounts

---

### 4. Suspicious Process Execution
```spl
index=main source="*Sysmon*" EventCode=1
| search (Image="*powershell.exe*" AND CommandLine IN ("*-enc*", "*-encoded*", "*downloadstring*", "*invoke-expression*"))
  OR (Image="*cmd.exe*" AND CommandLine="*/c*")
  OR (Image="*wmic.exe*" AND CommandLine="*process*call*create*")
| table _time, host, Image, CommandLine, User, ParentImage
| sort - _time
```
**Purpose:** Identify potentially malicious process execution patterns  
**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter

---

### 5. Registry Persistence Detection
```spl
index=main source="*Sysmon*" EventCode=13
| search TargetObject IN ("*\\Run*", "*\\RunOnce*", "*\\Winlogon\\*", "*\\Explorer\\*")
| table _time, host, TargetObject, Details, User, Image
| sort - _time
```
**Purpose:** Monitor registry modifications commonly used for persistence  
**MITRE ATT&CK:** T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys

---

## Key SPL Queries Library

### User Activity Analysis
```spl
index=main EventCode=4624
| stats count by Account_Name, Logon_Type, src_ip
| sort - count
```

### Failed Login Summary
```spl
index=main EventCode=4625
| stats count, values(src_ip) as source_ips by Account_Name
| where count > 3
| sort - count
```

### PowerShell Execution Tracking
```spl
index=main source="WinEventLog:Microsoft-Windows-PowerShell/Operational"
| stats count by host, EventCode
| sort - count
```

### New User Account Detection
```spl
index=main EventCode=4720
| table _time, host, Account_Name, Creator_User_Name
| sort - _time
```

### Sysmon Network Connection Analysis
```spl
index=main source="*Sysmon*" EventCode=3
| stats count by Image, DestinationIp, DestinationPort
| sort - count
```

---

## Investigation Methodology

### Phase 1: Initial Triage
1. Define investigation scope and time range
2. Identify relevant log sources and indexes
3. Assess event volume and data availability

### Phase 2: Indicator Identification
1. Search for known IOCs (IPs, domains, file hashes)
2. Hunt for suspicious patterns (anomalous accounts, processes)
3. Correlate events across multiple data sources

### Phase 3: Timeline Reconstruction
1. Establish initial compromise timeframe
2. Map adversary actions chronologically
3. Identify persistence mechanisms and lateral movement

### Phase 4: Impact Assessment
1. Determine affected systems and users
2. Assess data access and exfiltration risk
3. Identify compromised credentials

### Phase 5: Documentation & Remediation
1. Map findings to MITRE ATT&CK framework
2. Document evidence and chain of custody
3. Recommend detection improvements and remediation steps

---

## MITRE ATT&CK Techniques Analyzed

| Tactic | Technique ID | Technique Name | Detection Method |
|--------|--------------|----------------|------------------|
| Persistence | T1136.001 | Create Account: Local Account | Event ID 4720 monitoring |
| Persistence | T1547.001 | Registry Run Keys / Startup Folder | Sysmon Event ID 13 |
| Execution | T1059.001 | PowerShell | PowerShell Operational logs |
| Defense Evasion | T1027 | Obfuscated Files or Information | Encoded command detection |
| Command and Control | T1071.001 | Application Layer Protocol: Web | Network connection logs |

---

## Tools & Technologies

- **SIEM Platform:** Splunk Enterprise
- **Log Sources:** 
  - Windows Security Event Logs
  - Sysmon (System Monitor)
  - PowerShell Operational Logs
- **Analysis Tools:** 
  - CyberChef (payload decoding)
  - MITRE ATT&CK Navigator
- **Frameworks:** 
  - MITRE ATT&CK
  - Cyber Kill Chain

---

## Key Achievements

✅ **Comprehensive Splunk Trilogy Completion** - Basics → SPL → Investigation  
✅ **Real-World Investigation Experience** - Backdoor detection and analysis  
✅ **Detection Rule Development** - 5+ production-ready SPL queries  
✅ **MITRE ATT&CK Mapping** - Adversary TTP documentation  
✅ **Multi-Source Correlation** - Windows Security, Sysmon, PowerShell logs  
✅ **Threat Hunting Methodology** - Systematic investigation framework

---

## Next Steps

### Planned Enhancements
- [ ] Expand detection rule library (10+ rules covering additional TTPs)
- [ ] Build Splunk dashboards for real-time security monitoring
- [ ] Create alert automation workflows
- [ ] Document additional investigation case studies
- [ ] Integrate threat intelligence feeds for enrichment

### Continuous Learning
- TryHackMe SOC Level 1 pathway continuation
- Advanced SPL optimization techniques
- Splunk Enterprise Security app exploration
- SOAR (Security Orchestration, Automation, and Response) integration

---

## Portfolio Highlights for Resume

**SOC Analyst / Security Analyst Applications:**
> "Completed comprehensive Splunk SIEM training including real-world incident investigation, developed 5+ detection rules mapped to MITRE ATT&CK framework, and documented threat hunting methodology for backdoor detection across Windows environments."

**IT Support / Systems Analyst Applications:**
> "Demonstrated log analysis and security awareness through hands-on Splunk training, including investigation of suspicious user accounts, registry modifications, and malicious PowerShell execution. Documented systematic troubleshooting methodology and escalation criteria."

---

## Contact & Additional Work

**GitHub Portfolio:** [Cybersecurity-Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)  
**LinkedIn:** [Your LinkedIn Profile]

*This portfolio represents hands-on technical work completed through structured lab environments. All investigations follow responsible disclosure and ethical hacking principles.*


