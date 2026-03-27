# Mastercard Cybersecurity Virtual Experience - Phishing & Security Awareness

## Overview

I completed Mastercard's cybersecurity virtual internship focusing on phishing threat mitigation and security awareness training - critical capabilities for organizations defending against social engineering attacks. This experience provided hands-on practice designing realistic phishing simulations, analyzing campaign results, and developing targeted security awareness training for vulnerable teams.

Phishing remains the #1 initial access vector for cyber attacks, responsible for over 90% of successful breaches according to industry research. Understanding how attackers craft convincing phishing emails, how employees fall victim, and how to build organizational resilience through awareness training is essential for security operations. This project demonstrates ability to think like an attacker (offensive mindset), analyze risk data (analytical capability), and design effective countermeasures (defensive strategy).

**Connection to Security Operations:** In SOC environments, phishing investigations are among the most frequent incident types. Analysts must determine if reported emails are malicious, extract IOCs for blocking, and assess organizational impact. Understanding what makes phishing effective enables better detection, investigation, and prevention.

---

## Learning Objectives

Through this virtual internship, I developed capabilities in:

**Social Engineering Analysis:**
- Understanding psychological tactics attackers use to manipulate victims
- Identifying characteristics of effective vs. obvious phishing attempts
- Recognizing subtle indicators of legitimacy that bypass user skepticism
- Applying attacker tradecraft to security awareness testing

**Phishing Simulation Design:**
- Creating realistic phishing emails for security awareness campaigns
- Balancing believability with ethical simulation practices
- Masking malicious intent through professional communication
- Incorporating context relevant to target organization

**Data Analysis & Risk Assessment:**
- Analyzing phishing simulation metrics (open rates, click-through rates, success rates)
- Identifying high-risk teams requiring additional training
- Quantifying organizational vulnerability to social engineering
- Prioritizing security awareness efforts based on data

**Security Awareness Training:**
- Designing targeted training materials for vulnerable populations
- Translating technical threats into accessible educational content
- Creating actionable guidance for phishing identification
- Measuring training effectiveness through simulation campaigns

---

## Task 1: Phishing Email Simulation Design

### Understanding the Phishing Threat

**What Makes Phishing Dangerous:**

Phishing attacks succeed by exploiting human psychology rather than technical vulnerabilities:
- **Trust exploitation:** Impersonating legitimate sources (IT, HR, executives)
- **Urgency creation:** Time pressure prevents careful scrutiny
- **Fear induction:** Threat of account lockout, security breach, or disciplinary action
- **Authority invocation:** Instructions from "IT Security" or "Management"

**Organizational Impact:**

Successful phishing attacks enable:
- **Credential theft:** Account takeover and unauthorized system access
- **Malware delivery:** Ransomware, backdoors, spyware installation
- **Financial fraud:** Wire transfer scams, invoice manipulation
- **Data exfiltration:** Access to sensitive customer or business information

### Analyzing the "Obvious Fake"

**Original Phishing Email (Provided by Mastercard):**

```
From: mastercardsIT@gmail.com
To: employee@email.com
Subject: URGENT! Password Reset Required—

Body:
Hello (insert name),

Your email account has been compromised. immediate action is required to reset your password!

Click here to reset your password in the next hour or your account will be locked:
[https://en.wikipedia.org/wiki/Phishing]

Regards, Mastercard IT
```

**Red Flags Identified:**

1. **Suspicious sender address:** `mastercardsIT@gmail.com` (typo + Gmail domain, not corporate email)
2. **Poor grammar and capitalization:** "immediate action" (lowercase), inconsistent punctuation
3. **Sloppy formatting:** Spacing issues, missing professional structure
4. **Exposed suspicious URL:** Wikipedia link clearly visible (not company domain)
5. **Generic greeting:** "(insert name)" placeholder not replaced
6. **Vague threat:** No specific context about the "compromise"

**Why This Fails:**

Employees with basic security awareness training would immediately recognize multiple indicators of fraud. Modern phishing attacks are far more sophisticated, requiring defenders to understand advanced social engineering tactics.

### Designing an Improved Phishing Simulation

**My Redesigned Email:**

```
From: mastercardsIT@gmail.com
To: employee@email.com
Subject: URGENT! Password Reset Required—

Hello (Insert name),

During routine security monitoring, Mastercard IT Security detected unusual activity 
associated with your email account. As a precautionary measure, company policy requires 
an immediate password reset to secure your account and prevent potential unauthorized 
access to internal systems.

Please complete your password reset within the next hour using the link below. 
Failure to do so will result in temporary account suspension pending manual security review.

[https://en.wikipedia.org/wiki/Phishing]

We appreciate your prompt attention to this security matter.

Mastercard IT Security Team
```

**Improvements Applied:**

**1. Professional Tone & Grammar:**
- Corrected all capitalization and punctuation errors
- Used corporate communication style
- Structured paragraphs logically

**2. Added Legitimacy Indicators:**
- **"Routine security monitoring":** Implies normal operations, not panic
- **"Company policy requires":** Suggests legitimate compliance requirement
- **"Mastercard IT Security Team":** Proper department identification
- **Professional closing:** "We appreciate your prompt attention"

**3. Enhanced Psychological Manipulation:**
- **Authority:** IT Security department conducting "routine monitoring"
- **Urgency:** "within the next hour" creates time pressure
- **Fear:** "account suspension pending manual security review" threatens consequences
- **Legitimacy:** "precautionary measure" sounds procedural, not alarmist

**4. Subtle Context:**
- Specific but vague: "unusual activity" sounds technical without requiring details
- Process-oriented language: "company policy," "manual security review"
- Helpful tone: "to secure your account and prevent..." (protecting user)

**Additional Improvements Identified:**

Post-submission, I recognized further enhancements:
- **Mask hyperlink in plain text:** "Click here to reset password" instead of visible URL
- **Add support contact:** "If you have questions, contact IT Security at [number]"
- **Include confidentiality disclaimer:** Standard email footer for legitimacy
- **Use company branding:** Logo, signature block (if simulating internal email)

### Why This Improved Version Is Effective

**Bypasses Common Detection Methods:**

1. **Professional writing:** No obvious grammar/spelling errors to flag
2. **Contextual relevance:** References "routine monitoring" and "company policy"
3. **Measured urgency:** One hour deadline creates pressure without appearing desperate
4. **Authority framing:** IT Security conducting normal operations

**Exploits Psychological Vulnerabilities:**

1. **Compliance mindset:** Employees conditioned to follow IT directives
2. **Fear of consequences:** "Account suspension" motivates immediate action
3. **Trust in internal communications:** Assumes email from IT Security is legitimate
4. **Busy professionals:** Time pressure prevents careful URL verification

**Real-World Attack Comparison:**

This simulation mirrors actual phishing tactics used in successful breaches:
- Office 365 credential phishing campaigns use similar "account security" pretexts
- Attackers frequently impersonate IT departments for password reset requests
- Professional tone and formatting increase victim trust
- One-hour deadlines prevent consultation with IT before clicking

---

## Task 2: Phishing Simulation Results Analysis

### Campaign Metrics

**Simulation Results by Department:**

| Team | Email Open Rate | Click-Through Rate | Phishing Success Rate |
|------|----------------|-------------------|---------------------|
| **HR** | 100% | 85% | **75%** |
| **Marketing** | 65% | 40% | **38%** |
| Card Services | 60% | 50% | 10% |
| IT | 80% | 2% | 0% |
| Engineering | 70% | 4% | 1% |
| R&D | 50% | 5% | 2% |
| Reception | 40% | 10% | 0% |
| **Overall Average** | 66% | 28% | **18%** |

**Metric Definitions:**
- **Email Open Rate:** Percentage of recipients who opened the email
- **Click-Through Rate:** Percentage who clicked the phishing link
- **Phishing Success Rate:** Percentage who clicked AND entered credentials

### Data Analysis & Risk Identification

**High-Risk Teams Identified:**

**1. Human Resources (75% Success Rate)**
- **Critical vulnerability:** 3 out of 4 HR employees would fall for phishing
- **Business impact:** HR accesses sensitive employee data (SSNs, salaries, health info)
- **Attack value:** HR credentials enable identity theft, social engineering, and targeted attacks

**2. Marketing (38% Success Rate)**
- **Significant vulnerability:** More than 1 in 3 Marketing employees susceptible
- **Business impact:** Marketing manages customer data, brand communications, external partnerships
- **Attack value:** Compromised marketing accounts enable brand impersonation and customer targeting

**Lower-Risk Teams:**

**IT Department (0% Success Rate)**
- Technical staff trained to recognize phishing indicators
- Daily exposure to security concepts reduces susceptibility
- Expected outcome for security-aware team

**Engineering (1% Success Rate)**
- Technical mindset promotes critical evaluation of suspicious emails
- Regular interaction with code/systems develops skepticism

**Reception (0% Success Rate)**
- Possible factors: lower email volume, administrative training, or smaller sample size

### Root Cause Analysis

**Why HR and Marketing Are Vulnerable:**

**HR Characteristics:**
- **High email volume:** Constant communication with employees, applicants, vendors
- **Frequent external contacts:** Resumes, benefits providers, background check services
- **Trusting nature:** Job function requires helping people (exploitable trait)
- **Policy-oriented:** Conditioned to enforce "company policy" (used in phishing pretext)

**Marketing Characteristics:**
- **External focus:** Regular communication with customers, partners, agencies
- **Fast-paced environment:** Deadline pressure reduces scrutiny of emails
- **Creative vs. technical:** Less exposure to security/technical concepts
- **Campaign-driven:** Accustomed to urgent requests and time-sensitive actions

**Organizational Insight:**

Non-technical departments with high external communication are systematically more vulnerable to social engineering. Security awareness training must be role-specific, addressing unique risk factors for each team.

### Security Awareness Training Design

**Targeted Training for HR and Marketing:**

**Training Objectives:**
1. Recognize common phishing indicators specific to their roles
2. Verify requests through independent channels (not email links)
3. Understand business impact of credential compromise
4. Practice reporting suspicious emails promptly

**Training Content Developed:**

**Module 1: What is Phishing?**
- Definition and real-world examples
- Statistics on phishing as #1 attack vector
- Case studies of HR/Marketing-targeted campaigns

**Module 2: Common Phishing Tactics**
- **Authority exploitation:** Fake IT requests, executive impersonation
- **Urgency creation:** Deadline pressure to bypass scrutiny
- **Legitimacy indicators (fake):** Professional tone, company branding
- **Context relevance:** Tailored to recipient's role

**Module 3: How to Spot Phishing Emails**

**Visual Examples with Annotations:**
- Suspicious sender addresses (typos, wrong domains)
- Generic greetings vs. personalized communication
- Grammatical errors and formatting issues
- Mismatched URLs (hover to preview destination)
- Requests for credentials or sensitive information

**Module 4: What to Do**

**Clear Action Steps:**
1. **Don't click links** in unexpected emails requesting credentials
2. **Verify independently:** Call IT/sender using known phone number (not email contact)
3. **Check URL carefully:** Hover before clicking, look for misspellings
4. **Report immediately:** Forward to security@company.com, delete original
5. **When in doubt, ask IT:** Better safe than compromised

**Training Format Considerations:**

**Engagement Techniques:**
- Heavy use of visuals (annotated email examples)
- Interactive quizzes testing phishing recognition
- Short duration (15-20 minutes) to maintain attention
- Real examples from company's industry
- Gamification: "Spot the Phish" challenges

**Effectiveness Measurement:**

**Follow-Up Assessment:**
- Repeat phishing simulation 30 days post-training
- Target 50% reduction in success rate for HR and Marketing
- Track reporting rate (employees forwarding suspicious emails)
- Quarterly refresher campaigns to maintain awareness

---

## Skills Demonstrated

**Offensive Security Mindset:**
- Ability to think like an attacker and design convincing social engineering
- Understanding psychological manipulation tactics
- Recognizing what makes phishing effective vs. detectable

**Analytical Capabilities:**
- Data analysis of simulation metrics across departments
- Risk prioritization based on quantitative evidence
- Root cause analysis identifying vulnerability factors

**Communication & Training:**
- Translating technical threats into accessible educational content
- Designing role-specific awareness materials
- Creating actionable guidance for non-technical audiences

**Strategic Thinking:**
- Connecting simulation results to business risk
- Prioritizing training resources for highest-impact teams
- Planning iterative improvement through measurement

---

## Real-World Application to Security Operations

### SOC Phishing Investigation Workflow

**How This Training Applies to SOC Analyst Role:**

**Scenario: User Reports Suspicious Email**

**Investigation Steps Informed by This Training:**

1. **Analyze Email Headers:**
   - Check sender address for typos, wrong domains (learned from "obvious fake")
   - Verify SPF/DKIM/DMARC authentication (technical validation)
   - Identify spoofing or compromised accounts

2. **Assess Social Engineering Tactics:**
   - Identify psychological manipulation (urgency, authority, fear)
   - Recognize pretext relevant to organization (my simulation design experience)
   - Evaluate sophistication level (obvious vs. targeted)

3. **Extract Indicators of Compromise:**
   - Malicious URLs or attachment hashes
   - Sender IP addresses and mail servers
   - File names and metadata from attachments

4. **Determine Organizational Impact:**
   - How many employees received email?
   - Which departments targeted? (HR/Marketing = higher risk per my analysis)
   - Did anyone click or provide credentials?

5. **Containment & Remediation:**
   - Block sender addresses and malicious URLs
   - Quarantine email from other users' inboxes
   - Reset credentials for users who clicked
   - Document IOCs for MISP sharing (connecting to my threat intelligence training)

6. **Security Awareness Follow-Up:**
   - Notify affected users with educational guidance
   - Share example with organization as training opportunity
   - Update phishing simulations to include new tactics observed

### Connection to Other Security Projects

**Integration with MISP Threat Intelligence:**

From my MISP training, phishing IOCs can be shared:
- **Email Indicators:** Sender addresses, subject patterns, attachment names
- **Network Indicators:** Malicious URLs, credential harvesting domains
- **File Indicators:** Malware hashes from attachments
- **Behavioral Indicators:** Social engineering tactics and pretexts

**Tag with MITRE ATT&CK:**
- T1566.001 (Phishing: Spearphishing Attachment)
- T1566.002 (Phishing: Spearphishing Link)
- T1598 (Phishing for Information)

**Integration with Splunk SIEM Analysis:**

From my Splunk investigation training, phishing detection queries:

```spl
index=email_logs
| search subject="*password reset*" OR subject="*urgent*" OR subject="*account suspended*"
| stats count by sender_domain, recipient_dept
| where count > 10
```

Correlate email logs with:
- Authentication failures (credential harvesting attempts)
- Web proxy logs (users visiting phishing URLs)
- Endpoint logs (malware execution from attachments)

**Integration with Network Traffic Analysis:**

From my Wireshark training, phishing investigation includes:
- Capturing HTTP POST requests to credential harvesting sites
- Analyzing DNS queries to newly registered phishing domains
- Extracting malware payloads from network traffic for analysis

---

## Key Takeaways

**Understanding Social Engineering:**
- Phishing effectiveness relies on psychology, not technical sophistication
- Professional tone and contextual relevance bypass user skepticism
- Urgency, authority, and fear are primary manipulation tactics

**Data-Driven Security:**
- Metrics enable identification of high-risk populations
- Targeted training more effective than organization-wide generic content
- Continuous measurement validates training effectiveness

**Organizational Resilience:**
- Security awareness is iterative process, not one-time training
- Non-technical departments require role-specific education
- Phishing simulations build muscle memory for threat recognition

**Defensive Strategy:**
- Technical controls (email filtering, MFA) complement but don't replace awareness
- Reporting culture crucial - employees should feel safe reporting mistakes
- Lessons from attacks inform future simulations and training

---

## Portfolio Integration

**This Mastercard experience complements my existing security projects:**

**With MISP Threat Intelligence:**
- Phishing IOCs extracted from investigations shared via MISP
- Email indicators, malicious URLs, attachment hashes documented
- Community alerting for widespread phishing campaigns

**With Splunk SIEM Analysis:**
- Email log analysis identifies phishing campaigns
- Correlation with authentication logs detects credential theft
- Dashboards track phishing reports and organizational trends

**With Wireshark Network Analysis:**
- Packet captures reveal credential harvesting traffic
- HTTP POST analysis shows stolen data transmission
- DNS queries identify phishing infrastructure

**With MITRE ATT&CK Framework:**
- Phishing mapped to Initial Access tactics
- Social engineering techniques documented
- Detection analytics developed for phishing-related activity

This integrated approach demonstrates complete phishing defense lifecycle: **Awareness (Mastercard) → Detection (Splunk/Wireshark) → Response (MISP) → Framework Mapping (MITRE)**

---

## Resources

- **Forage Platform:** Mastercard Cybersecurity Virtual Experience
- **Mastercard Security Awareness Team:** Simulation campaign guidance
- **Industry Research:** Phishing statistics and trends
- **MITRE ATT&CK:** T1566 (Phishing) technique documentation

---

## Status: COMPLETED ✅

**Skills Validated:**
- Social engineering analysis and design
- Security awareness training development
- Data analysis and risk assessment
- Communication and education

This virtual internship demonstrates understanding of phishing threats from both attacker and defender perspectives - essential capability for SOC analysts investigating social engineering attacks and building organizational resilience through security awareness programs.
