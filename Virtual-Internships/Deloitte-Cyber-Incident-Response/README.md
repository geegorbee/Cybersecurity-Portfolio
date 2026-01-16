# Deloitte Cybersecurity Virtual Experience - Incident Response Investigation

## 🎯 Executive Summary

Conducted cyber incident response investigation for Daikibo Industrials, a global manufacturing client, following suspected data breach resulting in sensitive production status information being leaked to media. Analyzed 190+ pages of web server logs spanning 72 hours to identify the source of unauthorized data access.

**Key Finding:** Identified compromised user account (`mdB7yD2dp1BFZPontHBQ1Z`) conducting automated data exfiltration via API polling at precise 60-minute intervals across 4 global manufacturing facilities. Attack pattern indicated insider threat or credential compromise requiring VPN access to internal network.

---

## 📊 Project Overview

| **Aspect** | **Details** |
|------------|-------------|
| **Client** | Daikibo Industrials (Manufacturing) |
| **Incident Type** | Data Breach / Unauthorized Access |
| **Data Analyzed** | 190+ pages of web request logs |
| **Timeframe** | June 25-27, 2021 (72-hour window) |
| **Platform** | Forage (Deloitte Australia) |
| **Completion Date** | January 2026 |
| **Role** | Cyber Incident Response Analyst |

---

## 🔍 Skills Demonstrated

### **Technical Skills**
- **Log Analysis:** Parsed and analyzed large-scale web server logs (190+ pages)
- **Pattern Recognition:** Identified behavioral baselines and anomalous activity patterns
- **Threat Detection:** Distinguished automated vs. human user behavior through temporal analysis
- **Incident Response:** Applied IR methodology (identification, containment recommendations, evidence preservation)
- **Network Security:** Evaluated attack vectors based on network architecture (VPN, intranet access)

### **Analytical Skills**
- Baseline behavior establishment (normal user activity patterns)
- Temporal pattern correlation (precise interval detection)
- Behavioral anomaly detection (machine-like vs. human activity)
- Attack vector assessment (insider threat vs. external breach)
- Evidence-based conclusion development

### **Communication Skills**
- Security findings documentation
- Client-facing incident reporting
- Remediation recommendations
- Technical evidence presentation

---

## 🚨 The Incident

### **Background**
A major news publication revealed sensitive private information about Daikibo Industrials' manufacturing operations. Production issues had caused assembly line stoppages, disrupting supply chains dependent on Daikibo's products. The client suspected their new manufacturing status dashboard may have been compromised.

### **Investigation Objectives**
1. Determine if the alleged breach could have occurred from an attacker on the internet directly (without VPN access to Daikibo's intranet)
2. Analyze web request logs to identify suspicious user activity
3. Identify the compromised user account (if any)
4. Determine attack methodology and provide security recommendations

---

## 🔎 Key Findings

### **Finding 1: Attack Vector Analysis**
**Conclusion:** External internet-based attack was **NOT possible**

**Evidence:**
- Manufacturing status dashboard hosted on Daikibo's internal intranet
- No direct internet exposure
- VPN tunneling required for remote access
- Network architecture properly segmented

**Implication:** Breach indicates either:
- Compromised employee credentials with VPN access
- Insider threat (malicious employee/contractor)
- Credential theft via phishing or social engineering

---

### **Finding 2: Compromised User Account Identified**

**User ID:** `mdB7yD2dp1BFZPontHBQ1Z`  
**Source IP:** 192.168.0.101 (Internal network)  
**Activity Period:** June 25-27, 2021

**Attack Pattern Timeline:**

#### **Phase 1: Initial Reconnaissance (June 25, 16:14-16:18)**
Normal human browsing behavior observed:
- Manual login sequence
- Random timing between requests (18s, 51s, 39s intervals)
- Page resources loaded (CSS, JavaScript files)
- Selective factory queries (one at a time)
- Human-paced interaction patterns

#### **Phase 2: Automated Data Exfiltration (June 25, 17:00 - 23:00)**
Behavioral shift to automated activity:
```
17:00:48 → All 4 factories queried simultaneously
18:00:48 → All 4 factories queried (EXACTLY 60:00 later)
19:00:48 → All 4 factories queried (EXACTLY 60:00 later)
20:00:48 → All 4 factories queried (EXACTLY 60:00 later)
21:00:48 → All 4 factories queried (EXACTLY 60:00 later)
22:00:48 → All 4 factories queried (EXACTLY 60:00 later)
23:00:48 → All 4 factories queried (EXACTLY 60:00 later)
```

**Red Flag Indicators:**
- ❌ Precise 60-minute intervals (down to the second)
- ❌ No page resource requests (no CSS/JS loading)
- ❌ Simultaneous multi-factory queries (no human delay)
- ❌ Continued through session expiration
- ❌ No variation in timing (machine-like precision)

#### **Phase 3: Session Expiration & Script Persistence (June 26, 00:00-16:04)**
Script continued attempting queries despite authentication failure:
```
00:00:48 → 401 UNAUTHORIZED (session expired)
01:00:48 → 401 UNAUTHORIZED (script continues)
02:00:48 → 401 UNAUTHORIZED (script continues)
... [continues every hour] ...
15:00:48 → 401 UNAUTHORIZED (script continues)
```

**Key Observation:** Automated script lacked error handling to detect session expiration—continued blindly for 15+ hours receiving 401 errors.

#### **Phase 4: Script Re-Authentication (June 26, 16:04)**
Attacker manually re-authenticated, script resumed:
```
16:04:54 → Successful re-login
17:00:48 → Automated queries resume (4 factories)
18:00:48 → Continues automated pattern
```

---

### **Finding 3: Attack Methodology**

**Technique:** Automated API Data Collection  
**MITRE ATT&CK Mapping:** T1213.002 (Data from Information Repositories)

**Attack Characteristics:**
1. **Initial Access:** Legitimate user credentials (compromised or insider)
2. **Reconnaissance:** Manual exploration of dashboard functionality
3. **Collection:** Python/script-based automated API polling
4. **Exfiltration:** Systematic monitoring of all 4 manufacturing facilities
5. **Persistence:** Re-authentication when detected session expiration

**Targeted Data:**
- Meiyo factory status
- Seiko factory status
- Shenzhen factory status
- Berlin factory status

**Intent:** Competitive intelligence gathering or industrial espionage

---

## 📈 Comparison: Normal vs. Suspicious Activity

| **Indicator** | **Normal User (192.168.0.49)** | **Compromised User (192.168.0.101)** |
|---------------|--------------------------------|--------------------------------------|
| **Request Timing** | Random intervals (18s, 51s, 39s) | Exact 60:00 intervals |
| **Page Resources** | ✅ Loads CSS/JS files | ❌ None (direct API calls only) |
| **Query Pattern** | 1-2 specific factories | All 4 factories simultaneously |
| **Session Handling** | Normal logout behavior | ❌ Continues through expiration |
| **Factories Queried** | Selective (based on need) | Systematic (all facilities) |
| **Behavior Type** | Human (browsing, clicking) | Automated (scripted) |
| **Request Precision** | Variable human delays | Machine-precise timing |

---

## 💡 Security Recommendations

### **Immediate Actions (0-7 Days)**

1. **Account Response**
   - Disable user account `mdB7yD2dp1BFZPontHBQ1Z` immediately
   - Force password reset for all users with dashboard access
   - Conduct forensic analysis of compromised account activity history
   - Interview account owner to determine if credentials were stolen or insider threat

2. **Session Management Hardening**
   - Reduce session timeout from 24 hours to 2-4 hours for production systems
   - Implement idle timeout (30 minutes of inactivity)
   - Require re-authentication for sensitive API endpoints

3. **Rate Limiting Implementation**
   - Set maximum API requests per user per hour (e.g., 100 requests/hour)
   - Block users exceeding threshold temporarily (15-30 minutes)
   - Alert security team on rate limit violations

### **Short-Term Improvements (1-3 Months)**

4. **Behavioral Anomaly Detection**
   - Implement User and Entity Behavior Analytics (UEBA)
   - Define baseline patterns for legitimate dashboard usage
   - Alert on deviations: precise timing intervals, simultaneous queries, missing page resources
   - Flag machine-like behavior (sub-second precision in repeated actions)

5. **API Security Enhancement**
   - Require User-Agent headers on all API requests
   - Implement CAPTCHA or challenge-response for suspected automation
   - Add request fingerprinting to distinguish browsers from scripts
   - Log and alert on direct API access without corresponding UI interactions

6. **Enhanced Logging & Monitoring**
   - Expand log retention from current period to 90 days minimum
   - Implement real-time log analysis (SIEM integration)
   - Create detection rules for:
     - Repeated 401 errors from same user/IP (potential script persistence)
     - API calls without UI resource requests (automation indicator)
     - Exact time interval patterns (60:00 recurring)
     - Simultaneous multi-endpoint queries (bulk collection)

### **Long-Term Strategic Improvements (3-12 Months)**

7. **Zero Trust Architecture**
   - Implement continuous authentication verification
   - Require MFA for VPN and dashboard access
   - Apply principle of least privilege (limit users to their assigned factories only)
   - Geographic restriction policies (block access from unexpected locations)

8. **Data Loss Prevention (DLP)**
   - Classify manufacturing status data by sensitivity level
   - Implement data access controls based on job role
   - Monitor and restrict bulk data exports
   - Watermark sensitive information for leak tracing

9. **Insider Threat Program**
   - Conduct regular security awareness training
   - Implement user activity monitoring for high-risk roles
   - Establish anomalous behavior investigation procedures
   - Create incident response playbook for insider threats

10. **Third-Party Security Assessment**
    - Conduct external penetration testing of dashboard application
    - Perform red team exercise simulating insider threat scenario
    - Hire third-party to assess VPN security and network segmentation

---

## 🎓 Key Learnings

### **Technical Insights**

1. **Baseline Behavior is Critical**  
   Without understanding what "normal" looks like, detecting anomalies is nearly impossible. Establishing behavioral baselines for users, systems, and applications is foundational to threat detection.

2. **Automation Leaves Fingerprints**  
   Automated scripts exhibit distinct patterns that differ from human behavior:
   - Machine-precise timing (exact intervals)
   - Lack of variability (no human randomness)
   - Missing ancillary requests (page resources)
   - Persistent behavior despite errors

3. **Log Volume Requires Automation**  
   Analyzing 190+ pages manually is tedious and error-prone. Real-world scenarios would require:
   - SIEM tools (Splunk, ELK Stack, Azure Sentinel)
   - Automated pattern detection scripts
   - Data visualization for temporal analysis
   - Machine learning for anomaly detection at scale

4. **Session Management is a Security Control**  
   Weak session timeouts increase attacker dwell time. In this case, 24-hour sessions allowed the script to run uninterrupted for extended periods.

### **Incident Response Methodology**

Applied structured IR approach:
1. **Identification:** Detected anomalous patterns in logs
2. **Analysis:** Differentiated normal vs. malicious behavior
3. **Containment:** Recommended account disable and access restrictions
4. **Eradication:** Suggested credential resets and security hardening
5. **Recovery:** Proposed long-term monitoring and prevention measures
6. **Lessons Learned:** Documented findings and preventive recommendations

---

## 🔗 Connection to Professional Experience

### **Relevance to CRA Role (2018-Present)**

This incident response investigation directly parallels my work at Canada Revenue Agency:

**Access Monitoring & Anomaly Detection:**
- At CRA: Monitored identity verification and access request patterns for 100+ agents across multiple teams
- In Simulation: Analyzed web access patterns for manufacturing dashboard users
- **Skill Transfer:** Recognizing when authentication/access workflows deviate from baseline behavior

**Insider Threat Mitigation:**
- At CRA: Enforced RBAC, segregation of duties, and least-privilege principles
- In Simulation: Identified compromised internal account conducting data exfiltration
- **Skill Transfer:** Understanding that insider threats (intentional or compromised credentials) are often harder to detect than external attacks

**Compliance & Audit Support:**
- At CRA: Produced audit-ready documentation for identity verification processes and access control decisions
- In Simulation: Created evidence timeline and documented findings for client reporting
- **Skill Transfer:** Maintaining detailed logs, timestamps, and evidence trails for incident investigation

**Session & Authentication Lifecycle:**
- At CRA: Managed authentication workflows, access provisioning/deprovisioning
- In Simulation: Analyzed session expiration behavior and re-authentication patterns
- **Skill Transfer:** Understanding how authentication mechanisms can be exploited or circumvented

---

## 📁 Repository Structure

```
Deloitte-Cyber-Incident-Response/
├── README.md (this file)
├── SCENARIO.md (full task description & client background)
├── INVESTIGATION.md (detailed methodology & analysis approach)
├── FINDINGS.md (comprehensive evidence & attack timeline)
├── RECOMMENDATIONS.md (security improvements & remediation strategies)
└── assets/
    ├── log-analysis-diagram.png (visual timeline of attack pattern)
    └── behavioral-comparison-chart.png (normal vs. suspicious activity)
```

---

## 📝 Resume Summary

**Deloitte Australia Cybersecurity Virtual Experience - Incident Response Investigation (January 2026)**

Investigated suspected data breach at manufacturing client (Daikibo Industrials) by analyzing 190+ pages of web request logs spanning 72 hours; identified compromised user account (`mdB7yD2dp1BFZPontHBQ1Z`) conducting automated data exfiltration via API polling at exact 60-minute intervals across 4 global manufacturing facilities; determined attack vector required internal VPN access, indicating insider threat or credential compromise; provided security recommendations including enhanced session management, rate limiting, and behavioral anomaly detection.

**Skills Applied:** Log Analysis, Pattern Recognition, Threat Detection, Incident Response, Network Security, Behavioral Analysis, MITRE ATT&CK Framework

---

## 🏆 Certification

Completed through Forage platform - Deloitte Australia Cybersecurity Virtual Experience Program

**Certificate ID:** [Your certificate ID if available]  
**Completion Date:** January 2026  
**Platform:** [Forage - Deloitte Australia](https://www.theforage.com/)

---

## 📚 Additional Resources

**MITRE ATT&CK Techniques Referenced:**
- [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)
- [T1213.002: Sharepoint](https://attack.mitre.org/techniques/T1213/002/)

**Incident Response Frameworks:**
- [NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)
- [SANS Incident Response Process](https://www.sans.org/white-papers/33901/)

**Behavioral Analysis:**
- [User and Entity Behavior Analytics (UEBA)](https://www.gartner.com/en/information-technology/glossary/user-and-entity-behavior-analytics-ueba)

---

## 📧 Contact

**Gerald Brown**  
📧 gerald.brown@alumni.utoronto.ca  
💼 [LinkedIn](https://linkedin.com/in/gerald-brown-63168223a)  
🐙 [GitHub](https://github.com/geegorbee)  
🔒 [TryHackMe: CybrSerp3nt](https://tryhackme.com/p/CybrSerp3nt)

---

*This project demonstrates practical application of incident response methodology, log analysis, and threat detection skills in a real-world manufacturing security scenario.*
