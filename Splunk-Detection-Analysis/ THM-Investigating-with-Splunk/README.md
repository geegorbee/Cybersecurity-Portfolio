# Investigating with Splunk - SOC Analyst Investigation

## Scenario
SOC Analyst observed anomalous behaviors in Windows machine logs indicating potential adversary access and backdoor creation. Suspected host logs were ingested into Splunk (index: `main`) for investigation and threat hunting.

**Investigation Objective:** Identify indicators of compromise, trace attack chain, and document adversary TTPs.

---

## Investigation Methodology

### Phase 1: Initial Reconnaissance
- **Action:** Assessed total event volume and data sources
- **Finding:** 12,256 events ingested across multiple Windows hosts
- **Approach:** Established baseline before narrowing investigation scope

### Phase 2: User Account Anomaly Detection
**Indicator:** Suspicious user account creation activity

**Windows Event ID Leveraged:** `4720` (A user account was created)

```spl
index=main EventCode=4720
```

**Key Finding:**
- Identified newly created user account: `A1berto` (note: "1" instead of "l" - common impersonation technique)
- Associated host: `Michael.Beavin`
- Adversary attempted to impersonate legitimate user "Alberto" using character substitution

**TTPs Identified:**
- **MITRE ATT&CK:** T1136.001 (Create Account: Local Account)
- **Tactic:** Persistence
- **Technique:** Backdoor user creation for maintaining access

---

### Phase 3: Persistence Mechanism Analysis
**Indicator:** Registry modification associated with backdoor user

**Search Refinement:**
```spl
index=main host="Michael.Beavin" A1berto
| search source="WinEventLog:Microsoft-Windows-Sysmon/Operational"
```

**Key Finding:**
- Registry key modification detected via Sysmon logging
- Target Object: Registry path containing reference to `A1berto`
- **Purpose:** Established persistence through registry modification

**Analysis:**
- Sysmon Event ID 13 (Registry value set) captured modification
- Adversary configured registry to maintain backdoor user access
- Demonstrates understanding of Windows persistence mechanisms

---

### Phase 4: Command Execution Tracking
**Indicator:** Remote user creation command

**Search Strategy:**
```spl
index=main A1berto source="WinEventLog:Security"
| search ParentProcessName="*powershell.exe*"
```

**Key Finding:**
- Remote account creation via PowerShell: `net user` command observed
- Parent process: `powershell.exe`
- Command executed from remote system

**TTPs Identified:**
- **MITRE ATT&CK:** T1059.001 (Command and Scripting Interpreter: PowerShell)
- **Lateral Movement:** Remote execution capability demonstrated

---

### Phase 5: Authentication Attempt Analysis
**Indicator:** Login attempts from backdoor account

**Windows Event ID Searched:** `4624` (An account was successfully logged on)

```spl
index=main EventCode=4624 A1berto
```

**Key Finding:**
- **Zero successful logins** from backdoor account during investigation period
- **Assessment:** Backdoor creation detected before adversary could leverage access
- Early detection prevented account compromise

---

### Phase 6: PowerShell Execution Investigation
**Indicator:** Suspicious PowerShell activity on infected host

**Host Identified:** `James.browne`

**Search Query:**
```spl
index=main host="James.browne" source="WinEventLog:Microsoft-Windows-PowerShell/Operational"
```

**Key Findings:**
- 79 PowerShell-related events logged
- PowerShell logging enabled (good detective capability)
- Multiple execution events captured for analysis

**Analysis:**
- High volume of PowerShell events suggests scripted activity
- Logging configuration provided visibility into adversary actions

---

### Phase 7: Malicious Script Decoding
**Indicator:** Encoded PowerShell script initiating web request

**Investigation Approach:**
1. Identified base64-encoded PowerShell command in logs
2. Extracted encoded payload
3. Decoded using CyberChef (From Base64 recipe)

**Key Finding:**
- Decoded script revealed full URL of adversary infrastructure
- Web request initiated for command-and-control (C2) or data exfiltration
- URL defanged for safe documentation

**TTPs Identified:**
- **MITRE ATT&CK:** T1027 (Obfuscated Files or Information)
- **MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web Protocols)
- **Tactic:** Command and Control

---

## Investigation Summary

### Adversary Tactics, Techniques, and Procedures (TTPs)

| MITRE ATT&CK Tactic | Technique | Evidence |
|---------------------|-----------|----------|
| **Persistence** | T1136.001 - Create Account: Local Account | Backdoor user `A1berto` created |
| **Persistence** | Registry modification | Registry key updated for backdoor user |
| **Execution** | T1059.001 - PowerShell | Remote command execution via PowerShell |
| **Defense Evasion** | T1027 - Obfuscated Files or Information | Base64-encoded PowerShell script |
| **Command and Control** | T1071.001 - Web Protocols | HTTP/HTTPS request to adversary infrastructure |

### Compromised Hosts
1. **Michael.Beavin** - Backdoor user creation
2. **James.browne** - Malicious PowerShell execution

### Detection Gaps Identified
- No successful authentication alerts triggered (Event ID 4624 monitoring may need tuning)
- Registry modification alerts could be improved for faster detection

---

## Key SPL Queries Used

### 1. User Account Creation Detection
```spl
index=main EventCode=4720
| table _time, host, Account_Name, Creator_User_Name
| sort - _time
```

### 2. Registry Modification Analysis
```spl
index=main host="Michael.Beavin" A1berto source="*Sysmon*"
| search EventCode=13
| table _time, TargetObject, Details
```

### 3. PowerShell Command Tracking
```spl
index=main source="WinEventLog:Security" A1berto
| search ParentProcessName="*powershell.exe*"
| table _time, host, CommandLine, ParentProcessName
```

### 4. Authentication Attempt Monitoring
```spl
index=main EventCode=4624 Account_Name="A1berto"
| stats count by host, Logon_Type
```

### 5. PowerShell Operational Logging
```spl
index=main host="James.browne" source="WinEventLog:Microsoft-Windows-PowerShell/Operational"
| stats count by EventCode
| sort - count
```

---

## Skills Demonstrated

### SIEM Analysis
- Event correlation across multiple data sources
- Windows Event Log interpretation (Security, Sysmon, PowerShell)
- Timeline reconstruction of attack chain

### Threat Hunting
- Proactive search for persistence mechanisms
- Identification of impersonation attempts
- Encoded script analysis and decoding

### Incident Response
- Systematic investigation methodology
- MITRE ATT&CK framework mapping
- Evidence documentation and chain of custody

### Technical Knowledge
- Windows security event IDs (4720, 4624)
- Sysmon telemetry (Event ID 13)
- PowerShell logging and analysis
- Registry persistence techniques

---

## Lessons Learned

### What Went Well
✅ Sysmon logging provided critical visibility into registry modifications  
✅ PowerShell operational logging captured adversary script execution  
✅ Event ID correlation allowed reconstruction of full attack chain  
✅ Early detection prevented successful backdoor authentication

### Areas for Improvement
⚠️ Alert tuning needed for automated detection of similar activity  
⚠️ Could implement detection rule for character-substitution impersonation attempts  
⚠️ PowerShell script block logging would provide even better visibility  
⚠️ Consider implementing behavior-based analytics for anomalous PowerShell activity

---

## Recommended Detection Rules

Based on this investigation, the following detection rules would improve coverage:

### 1. Suspicious User Account Creation
```spl
index=main EventCode=4720
| eval account_lower=lower(Account_Name)
| search account_lower IN ("*admin*", "*test*", "*backup*", "*service*")
  OR account_lower LIKE "%[0-9]%"
| table _time, host, Account_Name, Creator_User_Name
```
**Purpose:** Detect user accounts with suspicious naming patterns (impersonation, test accounts, accounts with numbers)

### 2. Remote PowerShell Execution
```spl
index=main ParentProcessName="*powershell.exe*" 
  (CommandLine="*net user*" OR CommandLine="*Invoke-*")
| table _time, host, CommandLine, User
```
**Purpose:** Identify potentially malicious PowerShell commands executed remotely

### 3. Registry Persistence Monitoring
```spl
index=main source="*Sysmon*" EventCode=13
| search TargetObject IN ("*Run*", "*RunOnce*", "*Winlogon*")
| table _time, host, TargetObject, Details, User
```
**Purpose:** Detect registry modifications commonly used for persistence

---

## Tools & Technologies

- **SIEM Platform:** Splunk Enterprise
- **Log Sources:** Windows Security, Sysmon, PowerShell Operational
- **Analysis Tools:** CyberChef (for payload decoding)
- **Framework:** MITRE ATT&CK for TTP mapping

---

## Conclusion

This investigation demonstrates end-to-end SIEM-based threat hunting and incident investigation capabilities. By systematically analyzing Windows event logs, correlating across multiple data sources, and mapping adversary behavior to the MITRE ATT&CK framework, the investigation successfully:

- Identified two compromised hosts
- Documented adversary persistence mechanisms
- Prevented successful backdoor authentication
- Recommended detection improvements

**Investigation Outcome:** Threat contained, indicators documented, detection gaps identified for remediation.

