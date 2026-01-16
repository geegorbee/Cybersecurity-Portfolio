# SCENARIO: Daikibo Industrials Data Breach Investigation

## 📰 The Incident

### **Public Disclosure**
A major news publication has revealed sensitive private information about Daikibo Industrials' manufacturing operations. The leaked information included:
- Real-time production status across multiple global facilities
- Manufacturing equipment operational states
- Assembly line performance data
- Supply chain disruption details

### **Business Impact**
- Production problems caused assembly lines to stop operations
- Supply chain disruptions affecting downstream customers
- Competitive intelligence exposed to market
- Potential financial and reputational damage
- Regulatory compliance concerns (data protection, industrial espionage)

### **Security Suspicion**
Daikibo's internal IT security team suspects the security of their newly deployed manufacturing status dashboard may have been compromised. The dashboard was designed to provide internal stakeholders with real-time visibility into production operations across their global manufacturing network.

---

## 🏭 Client Background: Daikibo Industrials

### **Company Profile**
- **Industry:** Manufacturing (industrial equipment, automotive components)
- **Global Presence:** 4 manufacturing facilities
  - Meiyo Factory (Japan)
  - Seiko Factory (Japan)
  - Shenzhen Factory (China)
  - Berlin Factory (Germany)
- **Technology Stack:** Internal web-based dashboard for production monitoring

### **Dashboard Purpose**
The manufacturing status dashboard was developed to enable:
- Real-time monitoring of production line status
- Equipment performance tracking
- Rapid response to production issues
- Supply chain coordination
- Executive visibility into global operations

---

## 🎯 Your Role: Cyber Incident Response Analyst

You have been brought in as part of Deloitte's Cybersecurity team to investigate the suspected breach. Your expertise in log analysis and threat detection is critical to determining:

1. **How the breach occurred** (attack vector analysis)
2. **Who was responsible** (threat actor identification)
3. **What data was accessed** (scope of compromise)
4. **How to prevent future incidents** (security recommendations)

---

## 📋 Investigation Objectives

### **Objective 1: Attack Vector Assessment**
**Question:** Could the alleged breach have happened from an attacker on the internet directly (i.e., no access to Daikibo's VPN)?

**Context:**
- The manufacturing status dashboard was designed to be hosted on Daikibo's internal intranet
- Remote access is only possible through VPN tunneling
- Network architecture includes proper segmentation between internal and external networks

**Your Task:**
- Evaluate the network architecture documentation
- Determine if external internet-based attacks were possible
- Assess whether breach indicates insider threat or compromised credentials

---

### **Objective 2: Log Analysis & Threat Detection**
**Question:** Who is the user with the most suspicious activity?

**Provided Evidence:**
- `web_requests.log` file containing all HTTP requests to the dashboard
- Log period covers the timeframe when the alleged attack must have occurred
- Each log entry includes:
  - Timestamp (ISO 8601 format)
  - Source IP address (internal network)
  - HTTP method (GET, POST)
  - Request URI (page/API endpoint accessed)
  - User ID (if authenticated)
  - Response status code (200 SUCCESS, 401 UNAUTHORIZED, etc.)

**Your Task:**
- Inspect the web request logs systematically
- Identify patterns that deviate from normal user behavior
- Spot suspicious request sequences
- Recognize automated vs. human activity
- Pinpoint the compromised user account

---

## 📊 Log File Structure

### **Format Overview**
The `web_requests.log` file is structured as follows:

```
[BLOCK FOR IP ADDRESS 1]
IP: 192.168.0.X
TIME                     METHOD REQUEST                              STATUS
2021-06-25T16:00:00.000Z GET    "/login"                             200 (SUCCESS)
2021-06-25T16:00:01.000Z GET    "/login.css"                         200 (SUCCESS)
...

[EMPTY LINE SEPARATOR]

[BLOCK FOR IP ADDRESS 2]
IP: 192.168.0.Y
TIME                     METHOD REQUEST                              STATUS
...
```

### **Key Characteristics**
- **Blocks:** Divided by empty lines, each representing activity from a unique IP address
- **Static IPs:** Internal Daikibo network IPs are static (no DHCP changes)
- **Sorting:** Requests within each block are sorted chronologically
- **Authentication:** Authenticated requests include `{authorizedUserId: "..."}` parameter
- **Sessions:** No continuous polling/pushing—users must refresh page to get latest data
- **Session Expiration:** Sessions expire daily; new day requires new login

---

## 🔍 Analysis Hints

### **Normal User Behavior Indicators**
1. **Login Sequence:**
   - Request to "/" (unauthorized, redirected to login)
   - Request to "/login" page
   - Load page resources ("/login.css", "/login.js")
   - POST to "/login" (submit credentials)
   - Request to "/" (now authorized)
   - Load dashboard resources ("/index.css", "/index.js")

2. **Browsing Pattern:**
   - Random timing intervals between requests (human clicking delays)
   - Sequential navigation (one page/resource at a time)
   - Variability in request order and timing
   - Loading of page resources (CSS, JS files) before API calls

3. **API Usage:**
   - API requests follow UI interaction pattern
   - Requests for specific data (factory-by-factory, machine-by-machine)
   - Human-paced delays between queries
   - Session ends with logout or natural inactivity

### **Suspicious Activity Indicators**
1. **Automated Behavior:**
   - Precise timing intervals (e.g., exactly 60:00, 30:00, 15:00)
   - No variability in request patterns (machine-like precision)
   - Missing page resource requests (direct API calls without UI)
   - Simultaneous multi-resource queries (no human delay)

2. **Data Collection Patterns:**
   - Systematic querying of all resources (comprehensive data gathering)
   - Bulk API requests without corresponding UI interaction
   - Repeated queries at fixed intervals (automated polling)
   - Continued requests despite session expiration (script persistence)

3. **Anomalous Session Handling:**
   - Multiple consecutive 401 errors without re-authentication attempt
   - Requests continuing through session expiration
   - Immediate resumption after automatic re-login

---

## 🛠️ Investigation Methodology

### **Step 1: Establish Baseline**
- Review logs for several "normal" users
- Document typical login patterns
- Identify standard browsing sequences
- Note average time intervals between requests

### **Step 2: Pattern Analysis**
- Look for outliers in request timing
- Identify users with unusual request volumes
- Spot precise interval patterns (60:00, 30:00, etc.)
- Flag missing page resource loads

### **Step 3: Behavioral Correlation**
- Compare request sequences across users
- Identify deviations from normal workflow
- Correlate API calls with UI interactions
- Detect automation signatures (exact timing, no variability)

### **Step 4: Threat Actor Identification**
- Isolate user IDs with suspicious patterns
- Document evidence of automated behavior
- Reconstruct attack timeline
- Determine data access scope

### **Step 5: Attack Vector Confirmation**
- Verify if external internet access was possible
- Confirm VPN requirement for dashboard access
- Determine if insider threat or credential compromise
- Assess lateral movement potential

---

## 🎯 Expected Deliverables

### **Question 1: Attack Vector Assessment**
**Format:** Multiple choice answer

**Options:**
- A) Yes, the dashboard was directly accessible from the internet
- B) No, the attacker has no direct access to the status dashboard (VPN required)

**Required Reasoning:**
- Network architecture analysis
- Access control evaluation
- Security boundary assessment

---

### **Question 2: Threat Actor Identification**
**Format:** User ID submission

**Expected Output:**
- Specific user ID from log files (e.g., `mdB7yD2dp1BFZPontHBQ1Z`)

**Supporting Evidence Required:**
- Timeline of suspicious activity
- Behavioral indicators (automation, timing, patterns)
- Comparison to normal user baseline
- Attack pattern reconstruction

---

## 📈 Success Criteria

### **Investigation Quality Indicators**
✅ **Thorough Analysis:**
- Reviewed entire log file systematically
- Established clear baseline for normal behavior
- Documented specific evidence for conclusions

✅ **Accurate Threat Detection:**
- Correctly identified compromised user account
- Recognized automation signatures
- Distinguished between human and machine behavior

✅ **Sound Reasoning:**
- Evidence-based conclusions
- Logical attack vector assessment
- Clear articulation of findings

✅ **Actionable Recommendations:**
- Specific security improvements
- Realistic implementation timeline
- Addresses root causes (not just symptoms)

---

## 🔒 Real-World Relevance

### **Common Attack Scenarios**
This simulation reflects real-world incidents:

1. **Insider Threat Cases:**
   - Tesla (2018): Employee sabotage and data theft
   - Coca-Cola (2006): Trade secret theft by insider
   - NSA (2013): Edward Snowden classified data exfiltration

2. **Compromised Credentials:**
   - SolarWinds (2020): Hijacked software update mechanism
   - Colonial Pipeline (2021): VPN credential compromise
   - Uber (2016): Employee credential theft

3. **Manufacturing Sector Targeting:**
   - Industrial espionage (competitive intelligence)
   - Supply chain disruption
   - Intellectual property theft
   - Nation-state APT campaigns (e.g., Dragonfly targeting energy sector)

### **Industry Context**
Manufacturing companies are high-value targets because:
- Production data reveals competitive advantages
- Supply chain visibility enables market manipulation
- Operational disruption causes significant financial damage
- Intellectual property is often insufficiently protected
- Legacy systems may lack modern security controls

---

## 📚 Related Frameworks & Standards

### **MITRE ATT&CK Tactics**
- **Initial Access:** Valid Accounts (T1078)
- **Discovery:** System Network Configuration Discovery (T1016)
- **Collection:** Data from Information Repositories (T1213)
- **Exfiltration:** Exfiltration Over Alternative Protocol (T1048)

### **NIST Cybersecurity Framework**
- **Identify:** Asset Management (ID.AM)
- **Detect:** Anomalies and Events (DE.AE)
- **Respond:** Analysis (RS.AN)
- **Recover:** Improvements (RC.IM)

### **ISO 27001 Controls**
- A.9.2.1: User Registration and De-registration
- A.9.4.1: Information Access Restriction
- A.12.4.1: Event Logging
- A.16.1.4: Assessment of and Decision on Information Security Events

---

## 📧 Client Expectations

### **Communication Requirements**
- **Clarity:** Non-technical executives need to understand findings
- **Evidence-Based:** All conclusions must be supported by log data
- **Actionable:** Recommendations must be specific and implementable
- **Timely:** Incident response requires rapid analysis and reporting

### **Reporting Deliverables**
1. **Executive Summary:** High-level findings and impact assessment
2. **Technical Analysis:** Detailed evidence and attack reconstruction
3. **Remediation Plan:** Prioritized security improvements
4. **Lessons Learned:** Process improvements for future prevention

---

*This scenario is based on the Deloitte Australia Cybersecurity Virtual Experience Program available on Forage. It simulates real-world incident response investigation in a manufacturing environment.*
