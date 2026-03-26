# MISP - Malware Information Sharing Platform

## Overview

I completed hands-on training with MISP (Malware Information Sharing Platform), an open-source threat intelligence platform used by security operations centers, threat intelligence teams, and incident response organizations worldwide to collect, store, and share threat information and Indicators of Compromise (IOCs). This training provided practical experience in structured threat information sharing - a critical capability for threat intelligence analysts working in collaborative security environments.

MISP enables security teams to move beyond isolated incident response by creating a distributed threat intelligence sharing model where organizations can contribute and consume threat data within trusted communities. Understanding how to effectively use MISP for IOC management, event correlation, and threat information distribution is essential for modern threat intelligence operations.

---

## Learning Objectives

Through this hands-on lab, I developed capabilities in:

**Threat Information Management:**
- Creating and managing security events with contextually linked IOCs
- Structuring threat data using MISP's event-attribute-object model
- Adding technical indicators (IP addresses, file hashes, domains) to events
- Attaching malware samples and analysis artifacts securely

**Collaborative Intelligence Sharing:**
- Understanding distribution models (organization-only, community, connected communities, all communities)
- Configuring appropriate sharing levels based on sensitivity and trust
- Using sharing groups for targeted threat information distribution
- Publishing events for consumption by partner organizations

**Threat Categorization & Enrichment:**
- Applying taxonomies for consistent threat classification
- Using tags to enable automated processing and correlation
- Leveraging feeds for continuous threat intelligence updates
- Implementing tagging best practices (TLP, confidence, origin, PAP)

**Integration & Automation:**
- Exporting IOCs to NIDS/SIEM platforms for automated detection
- Understanding MISP's API for programmatic intelligence consumption
- Correlating attributes across events to identify threat patterns
- Using event graphs to visualize relationships between indicators

---

## Platform Capabilities

### Core MISP Functionality

**IOC Database:**
MISP provides centralized storage for technical and non-technical threat indicators including IP addresses, domain names, file hashes, email addresses, URLs, malware samples, and adversary TTPs. This structured approach enables systematic threat tracking and historical analysis.

**Automatic Correlation:**
The platform automatically identifies relationships between attributes across different events, revealing connections between seemingly isolated incidents. This correlation capability is critical for identifying coordinated campaigns and linking threat actor activity.

**Distribution Models:**
MISP supports flexible information sharing:
- **Your organization only:** Internal threat intelligence
- **This community only:** Trusted MISP instance sharing
- **Connected communities:** Two-hop federation
- **All communities:** Global threat intelligence sharing

**Import/Export Integration:**
Events and indicators can be exported to NIDS (Snort, Suricata), SIEM platforms (Splunk, QRadar), and other security tools using standard formats (STIX, OpenIOC, CSV). This enables automated defensive action based on shared intelligence.

---

## Hands-On Scenario: Emotet Epoch 4 Investigation

### Event Creation & Management

I created a MISP event documenting an Emotet Epoch 4 infection chain involving CobaltStrike post-exploitation and spambot activity, based on real-world malware traffic analysis.

**Event Details Configured:**
- **Threat Type:** Phishing Email (initial infection vector)
- **Date:** Infection timeline based on malware traffic capture
- **Risk Level:** High (banking trojan with lateral movement capability)
- **Distribution:** This Community (sharing with trusted MISP partners)
- **Analysis Status:** Completed (full infection chain documented)

**Event Context:**
Emotet represents a sophisticated malware-as-a-service operation using phishing emails for initial access, followed by credential theft, lateral movement, and deployment of secondary payloads including CobaltStrike beacons. Documenting this infection chain in MISP enables partner organizations to detect and block similar campaigns.

### Adding Attributes: IOC Documentation

I populated the event with technical indicators extracted from the infection analysis:

**Network Indicators Added:**
- **C2 IP Addresses:** Emotet Epoch 4 command-and-control servers
  - Type: `ip-dst` (destination IP)
  - IDS Flag: Enabled (for NIDS signature generation)
  - Category: Network activity
  
- **Domain Names:** CobaltStrike infrastructure
  - Type: `domain`
  - IDS Flag: Enabled
  - Category: Network activity

**File Indicators Added:**
- **Malware Hashes:** SHA256 values for Emotet dropper and CobaltStrike beacon
  - Type: `sha256`
  - IDS Flag: Enabled
  - Category: Payload delivery

**Email Indicators Added:**
- **Sender Addresses:** Phishing campaign source emails
  - Type: `email-src`
  - Category: Payload delivery

**Batch Import Capability:**
For multiple indicators of the same type (e.g., a list of C2 IP addresses), MISP supports batch import by entering line-separated values in a single attribute field. This streamlines IOC ingestion from external threat reports.

### Malware Sample Attachment

I attached the CobaltStrike executable binary as a malware sample to the event:

**Security Measures Applied:**
- Marked file as malware (checkbox enabled)
- MISP automatically ZIP-encrypted the sample with password protection
- Prevents accidental download and execution by analysts
- Enables malware researchers to safely retrieve samples for analysis

This demonstrates proper handling of malicious artifacts in collaborative intelligence platforms - balancing accessibility for legitimate research with safety controls.

### Taxonomy & Tagging

I applied structured tags to classify the event for automated processing and filtering:

**Traffic Light Protocol (TLP):**
- **Tag Applied:** `tlp:amber`
- **Meaning:** Limited distribution - share only with members of your community
- **Rationale:** Emotet campaigns are active threats; controlled sharing prevents adversary awareness

**Confidence Level:**
- **Tag Applied:** `admiralty-scale:a2` (Probably True)
- **Meaning:** Indicators are from analysis of actual malware traffic
- **Rationale:** High confidence based on validated network capture, not unverified reporting

**Adversary Classification:**
- **Tag Applied:** `misp-galaxy:threat-actor="Mealybug"`
- **Meaning:** Links event to known Emotet threat actor group
- **Rationale:** Enables correlation with historical Emotet campaigns

**MITRE ATT&CK Mapping:**
- **Tag Applied:** `mitre-attack-pattern:T1566.001` (Spearphishing Attachment)
- **Meaning:** Documents initial access technique
- **Rationale:** Connects MISP event to ATT&CK framework for TTP-based analysis

### Tagging Best Practices Applied

**Event-Level vs Attribute-Level Tagging:**
I applied tags at the event level to classify the overall incident (TLP, confidence, threat actor). Attribute-level tags were used only for exceptions - for example, marking specific IPs as "sinkholed" when they were no longer active C2 servers.

**Minimal Subset Implementation:**
Every event included the four critical tag categories:
1. **TLP:** Information sharing boundaries
2. **Confidence:** Data quality and trustworthiness  
3. **Origin:** Source of intelligence (manual analysis vs automated feed)
4. **PAP (Permissible Actions Protocol):** How data can be used operationally

This tagging discipline ensures recipients understand intelligence provenance and handling requirements.

---

## Feeds & Continuous Intelligence

### Threat Intelligence Feeds

MISP integrates with external threat feeds providing continuous updates on:
- **Emerging malware campaigns**
- **Newly identified C2 infrastructure**  
- **Compromised credentials and breach data**
- **Adversary infrastructure (phishing domains, exploit kits)**

**Feed Preview Capability:**
Before importing feed events, analysts can preview attributes and objects to assess relevance. This prevents noise from automated import of irrelevant intelligence.

**Selective Import:**
Rather than bulk-importing entire feeds, analysts can select specific events matching organizational threat profile. For example, importing only Emotet-related indicators when banking trojans are priority threats.

**Correlation Analysis:**
When feed events are imported, MISP automatically correlates their attributes with existing organizational events, revealing previously unknown connections between internal incidents and external campaigns.

### Practical Feed Usage

In the aviation sector threat intelligence scenario from my MITRE training, I would configure MISP to:
1. Subscribe to aviation-sector-focused feeds (ICS-CERT, sector ISACs)
2. Import events tagged with relevant industries
3. Correlate imported indicators with internal security events
4. Export matched indicators to SIEM for automated detection

This creates a feedback loop: external intelligence informs internal detection, while internal incident data enriches shared intelligence.

---

## MISP Terminology & Data Model

### Events
Collections of contextually related threat information. Each event represents an incident, campaign, or threat actor activity.

**Example:** "Emotet Epoch 4 Infection Chain - CobaltStrike Deployment"

### Attributes  
Individual data points within an event (IP addresses, hashes, domains, email addresses).

**Example:** `45.142.212.61` (Emotet C2 IP address)

### Objects
Custom compositions of multiple related attributes.

**Example:** "Email object" containing sender address, subject line, attachment hash, and recipient

### Object References
Relationships between different objects showing attack progression.

**Example:** Phishing email object → Malware sample object → C2 infrastructure object

### Sightings
Time-stamped observations of an indicator in the wild, providing recency and prevalence data.

**Example:** Emotet C2 IP sighted in network traffic on [timestamp]

### Galaxies
Knowledge base elements for threat actor groups, malware families, tools, and techniques.

**Example:** Linking event to "Emotet" malware galaxy and "Mealybug" threat actor galaxy

---

## Integration with Detection Systems

### NIDS Export (Network Intrusion Detection)

MISP can export indicators flagged for IDS usage to Snort/Suricata rule format:

```
alert ip any any -> 45.142.212.61 any (msg:"MISP Event #123 - Emotet Epoch 4 C2"; reference:url,https://misp.local/events/123; sid:1000001;)
```

This enables automated blocking of known-malicious IPs at the network perimeter.

### SIEM Integration

For Splunk integration (connecting to my Splunk investigation projects):

**Search Query Example:**
```spl
index=firewall dest_ip IN (misp_ioc_list)
| lookup misp_events ip AS dest_ip OUTPUT event_id, threat_level, threat_actor
| where threat_level="high"
```

This correlates network traffic with MISP threat intelligence, automatically enriching security events with threat context.

### API-Driven Automation

MISP's RESTful API enables programmatic intelligence retrieval:

```python
# Pseudocode: Fetch high-confidence Emotet indicators
response = misp_api.search(
    tags=["tlp:amber", "malware:emotet"],
    confidence_min=75,
    date_from="2024-01-01"
)
```

This supports automated threat hunting workflows where fresh IOCs are continuously ingested into detection tools.

---

## Real-World Application Scenarios

### Scenario 1: Incident Response Intelligence Sharing

**Situation:** My organization detects Emotet infection.

**MISP Workflow:**
1. Create event documenting infection timeline, initial vector, compromised systems
2. Add extracted IOCs (C2 IPs, malware hashes, phishing sender addresses)
3. Tag with TLP:Amber (community sharing), high confidence
4. Map to MITRE ATT&CK techniques (T1566.001, T1059.001, T1055)
5. Publish to community MISP for partner notification
6. Monitor for sightings from other organizations indicating campaign spread

**Value:** Partner organizations receive early warning before Emotet reaches their networks.

### Scenario 2: Proactive Threat Hunting

**Situation:** External feed reports new CobaltStrike infrastructure.

**MISP Workflow:**
1. Import feed event with CobaltStrike C2 domains
2. MISP auto-correlates with my organization's previous Emotet event (both used CobaltStrike)
3. Correlation suggests adversary infrastructure overlap
4. Export new domains to SIEM for historical log analysis
5. Identify previously undetected beacon traffic in archived network logs
6. Create new event documenting historical compromise
7. Share findings back to community

**Value:** Retrospective threat hunting using shared intelligence uncovers hidden compromises.

### Scenario 3: Malware Analysis Collaboration

**Situation:** Reverse engineering team analyzes new banking trojan variant.

**MISP Workflow:**
1. Create event for malware family with initial static analysis results
2. Attach malware sample (ZIP-encrypted) for distribution to partner researchers
3. Add extracted IOCs as attributes (C2 infrastructure, persistence mechanisms)
4. Tag with confidence:low initially (early analysis stage)
5. As dynamic analysis progresses, update event with behavioral indicators
6. Increase confidence level as analysis confirms findings
7. Link to related malware galaxy entries and threat actor profiles

**Value:** Collaborative malware research where multiple organizations contribute analysis findings.

---

## Connection to Broader Threat Intelligence Workflow

### Integration with MITRE ATT&CK

MISP events are enriched by mapping to ATT&CK techniques:
- **Emotet Initial Access:** T1566.001 (Spearphishing Attachment)
- **Emotet Execution:** T1059.001 (PowerShell)  
- **CobaltStrike C2:** T1071.001 (Web Protocols)
- **Credential Access:** T1003 (OS Credential Dumping)

This enables TTP-based correlation: "Show me all MISP events involving T1566.001 AND T1055" reveals campaigns using similar attack patterns regardless of specific IOC values.

### Integration with Detection Engineering

The CAR (Cyber Analytics Repository) analytics from my MITRE training can be enhanced with MISP data:

**CAR-2020-09-001 Detection + MISP:**
```spl
# Original CAR detection for scheduled task abuse
index=sysmon EventCode=13 TargetObject="*\\Tasks\\*"

# Enhanced with MISP threat intelligence
| lookup misp_hashes file_hash AS FileHash OUTPUT threat_actor, campaign
| where isnotnull(threat_actor)
```

This combines behavior-based detection (suspicious scheduled tasks) with threat intelligence context (known malware hashes), reducing false positives and providing instant attribution.

### Integration with Splunk Investigations

My "Investigating with Splunk" project documented backdoor user creation and PowerShell abuse. If that investigation had been real (not a lab), the MISP workflow would be:

1. Document investigation findings in MISP event
2. Add IOCs discovered (backdoor username `A1berto`, PowerShell script hashes, C2 URLs)
3. Tag with MITRE techniques identified (T1136.001, T1059.001, T1027)
4. Share with community
5. Enable correlation if other organizations see similar activity

This closes the loop: investigation → documentation → sharing → collective defense.

---

## Skills Demonstrated

**Threat Information Management:**
- Structured event creation following intelligence reporting standards
- IOC extraction and categorization from malware analysis
- Secure handling of malicious artifacts
- Event lifecycle management (creation → enrichment → publishing)

**Collaborative Intelligence Operations:**
- Understanding of trust models and information sharing boundaries
- Application of TLP, confidence, and PAP frameworks
- Community-based threat intelligence contribution
- Consumption of external threat feeds

**Technical Integration:**
- NIDS/SIEM export for automated defensive action
- API-driven intelligence retrieval workflows
- Event correlation and pattern recognition
- Multi-source intelligence fusion

**Analytical Capabilities:**
- Connecting disparate indicators to reveal campaign patterns
- Threat actor attribution through infrastructure correlation
- Temporal analysis via sightings data
- TTP-based threat categorization using ATT&CK mapping

---

## Key Takeaways

**Operational Insights:**
1. **Structured sharing is force multiplication:** One organization's incident becomes collective defensive intelligence
2. **Context matters as much as indicators:** TLP, confidence, and origin determine intelligence usability
3. **Automation amplifies intelligence:** SIEM/NIDS integration turns passive intelligence into active defense
4. **Correlation reveals hidden patterns:** Seemingly unrelated events connect through shared infrastructure

**Technical Understanding:**
- MISP's event-attribute-object model provides flexible threat documentation
- Taxonomies and galaxies enable machine-readable threat classification
- Distribution models balance security with collaborative defense needs
- API automation enables intelligence-driven security operations

**Connection to Threat Intelligence Analyst Role:**

MISP proficiency addresses critical threat intelligence competencies:
- **Intelligence Collection:** Ingesting IOCs from multiple sources (feeds, analysis, incidents)
- **Intelligence Processing:** Structuring raw data into actionable threat information
- **Intelligence Analysis:** Correlating events to identify campaigns and threat actors  
- **Intelligence Dissemination:** Sharing findings with appropriate communities
- **Intelligence Application:** Exporting to detection systems for defensive action

Combined with MITRE ATT&CK framework expertise, MISP capabilities enable end-to-end threat intelligence operations: identifying threats → mapping to frameworks → sharing intelligence → enabling detection.

---

## Portfolio Integration

**MISP complements my existing security projects:**

**With Splunk Analysis:**
- Export MISP indicators to Splunk for threat hunting
- Enrich Splunk detections with MISP threat context
- Document Splunk investigation findings in MISP for sharing

**With MITRE Framework:**
- Tag MISP events with ATT&CK technique IDs
- Use Navigator to visualize threat coverage from MISP events
- Link CAR detection analytics to relevant MISP threat intelligence

**With AWS Security:**
- Share cloud infrastructure abuse indicators via MISP
- Consume threat feeds for S3 bucket scanning and access monitoring
- Document cloud security incidents for community awareness

This integrated approach demonstrates ability to operate across the full threat intelligence lifecycle using industry-standard platforms and methodologies.

---

## Resources

- **TryHackMe Room:** MISP - Malware Information Sharing Platform
- **MISP Project:** https://www.misp-project.org/
- **MISP Book:** https://www.circl.lu/doc/misp/
- **MISP Training:** CIRCL Training Modules
- **Sample Source:** malware-traffic-analysis.net (Emotet infection PCAP)

---

## Status: COMPLETED ✅

**Next Steps:**
- OpenCTI (Collaborative Threat Intelligence Platform)
- TheHive (Security Incident Response Platform)  
- Threat Intelligence Tools (YARA, Sigma, etc.)

This hands-on experience with MISP demonstrates practical threat intelligence platform operations - essential capabilities for collaborative security operations and community-based threat defense.
