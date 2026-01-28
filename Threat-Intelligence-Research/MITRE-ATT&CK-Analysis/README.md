MITRE ATT&CK FRAMEWORK - THREAT INTELLIGENCE FOUNDATION

Overview
I completed TryHackMe’s comprehensive MITRE framework room to build foundational knowledge of industry-standard threat intelligence frameworks and methodologies. This training covered the MITRE ATT&CK® framework, Cyber Analytics Repository (CAR), D3FEND, and related tools - all critical resources for threat intelligence analysts, SOC operations, and security researchers.
MITRE’s frameworks provide the common language and structured approach that threat intelligence professionals use to analyze adversary behavior, develop detection strategies, and communicate security findings across organizations. Understanding these frameworks is essential for translating raw threat data into actionable intelligence.

Learning Objectives
Through this lab, I developed capabilities in:
∙ MITRE ATT&CK® Framework: Understanding the structure, taxonomy, and application of the world’s most widely-used adversary behavior knowledge base
∙ Threat Intelligence Mapping: Translating threat actor activity into structured TTPs (Tactics, Techniques, Procedures)
∙ ATT&CK Navigator: Using the visualization tool to analyze threat groups and coverage gaps
∙ Detection Development: Leveraging CAR (Cyber Analytics Repository) to create detection analytics
∙ Defensive Frameworks: Understanding D3FEND’s defensive countermeasure taxonomy
∙ Adversary Emulation: Exploring Caldera and emulation planning resources

Key Frameworks Covered
1. MITRE ATT&CK® Framework
What it is:
A globally-accessible knowledge base documenting adversary tactics and techniques based on real-world observations. ATT&CK provides the common language for describing how attackers operate across the cyber kill chain.
Framework Structure - Understanding TTPs:
Tactics: The adversary’s goal or objective (the “why”)
∙ Example: Reconnaissance, Initial Access, Persistence, Privilege Escalation
Techniques: How the adversary achieves their objective (the “how”)
∙ Example: Active Scanning, Phishing, Scheduled Task/Job
Procedures: The specific implementation of a technique
∙ Example: Using Nmap for IP scanning, crafting spearphishing emails with malicious attachments
Why this matters for threat intelligence:
Understanding TTPs allows analysts to abstract specific incidents into patterns. Rather than tracking “organization X was compromised via a Word macro,” we can identify “adversary used T1566.001 (Phishing: Spearphishing Attachment)” - enabling pattern recognition across multiple incidents and proactive defense.

2. ATT&CK Matrix and Navigator
The ATT&CK Matrix:
A visual representation organizing all tactics (columns) and techniques (rows) into a comprehensive framework. The Enterprise matrix covers Windows, Linux, macOS, and cloud environments. Specialized matrices exist for Mobile and Industrial Control Systems (ICS).
ATT&CK Navigator:
An interactive tool for annotating and exploring matrices. Security teams use Navigator to:
∙ Visualize threat group behavior patterns
∙ Map detection coverage across their environment
∙ Identify defensive gaps
∙ Plan red team emulation exercises
Practical Application - Technique Deep Dive:
I analyzed the Active Scanning (T1595) technique as an example of the framework’s structure:
Tactic: ReconnaissanceTechnique: Active Scanning Sub-techniques:
∙ T1595.001 - Scanning IP Blocks
∙ T1595.002 - Vulnerability Scanning
∙ T1595.003 - Wordlist Scanning
Each technique page includes:
∙ Detailed descriptions and examples
∙ Procedure examples (real-world group usage)
∙ Mitigations (how to prevent/reduce effectiveness)
∙ Detection strategies (how to identify the technique)
∙ References to threat reports and research
This structure transforms abstract threat intelligence into actionable defensive guidance.

3. Cyber Kill Chain Integration
The training connected MITRE ATT&CK to Lockheed Martin’s Cyber Kill Chain, showing how tactics map to attack stages:
Kill Chain Stage → ATT&CK Tactics:
1. Reconnaissance
2. Weaponization → Resource Development
3. Delivery → Initial Access
4. Exploitation → Execution
5. Installation → Persistence, Privilege Escalation
6. Command & Control
7. Actions on Objectives → Exfiltration, Impact
Why this matters:
Understanding both frameworks enables analysts to communicate with different audiences. Some organizations use Kill Chain terminology; others prefer ATT&CK. Fluency in both enables effective translation of threat intelligence across teams and vendors.

Threat Intelligence in Practice
Threat Group Analysis - Mustang Panda (G0129)
I conducted hands-on analysis of Mustang Panda, an APT group targeting government entities, non-profits, and NGOs, using the ATT&CK Navigator to visualize their TTPs:
Key Findings from Mustang Panda Analysis:
Initial Access:
∙ T1566 - Phishing (primary technique)
∙ Spearphishing attachments targeting specific individuals
∙ Exploits trust relationships for credential harvesting
Persistence:
∙ T1053 - Scheduled Task/Job
∙ Maintains access through automated task execution
∙ Enables continued operation even after system reboots
Defense Evasion:
∙ T1027 - Obfuscated Files or Information
∙ Uses file obfuscation to evade signature-based detection
∙ Makes static analysis more difficult
Command and Control:
∙ T1105 - Ingress Tool Transfer
∙ Downloads additional tools post-compromise
∙ Enables capability expansion without initial payload bloat
Intelligence Value:
This analysis demonstrates how ATT&CK transforms disparate incident data into structured intelligence. Rather than just knowing “Mustang Panda uses phishing,” we understand their complete operational pattern - enabling defenders to implement layered detections across multiple attack stages.

Aviation Sector Threat Intelligence Scenario
The training included a practical scenario: acting as a security analyst for an aviation organization migrating to the cloud, I used ATT&CK’s Groups section to identify APT groups targeting the aviation sector and assess defensive gaps.
Methodology Applied:
1. Sector-Specific Threat Identification: Used ATT&CK Groups database to identify aviation-targeting adversaries
2. TTP Mapping: Analyzed each group’s preferred tactics and techniques
3. Coverage Gap Analysis: Used Navigator to visualize which techniques lack detection coverage
4. Cloud Migration Risk Assessment: Identified techniques specifically targeting cloud environments
5. Prioritization: Ranked techniques by likelihood and potential impact for aviation sector
This exercise demonstrated real-world threat intelligence workflow:
∙ Understanding your sector’s threat landscape (not all threats are equally relevant)
∙ Using structured frameworks to analyze adversary capabilities
∙ Translating intelligence into defensive priorities
∙ Risk-based approach to security investments

Detection Engineering - Cyber Analytics Repository (CAR)
What CAR Provides:
The Cyber Analytics Repository translates ATT&CK techniques into ready-made detection analytics. Each analytic explains:
∙ What to detect (the adversary behavior)
∙ Why it matters (the security impact)
∙ How to detect it (example queries for SIEM platforms)
Practical Example - CAR-2020-09-001: Scheduled Task - File Access
I analyzed this analytic which detects adversaries using scheduled tasks for persistence:
The Detection Logic:
Monitors file access patterns to scheduled task directories, identifying unauthorized task creation or modification.
Implementation Examples Provided:
Pseudocode (Human-Readable Logic):

processes = search Process:Create
schtasks_processes = filter processes where (exe == "schtasks.exe")
file_accesses = search FileAccess:Read
schtasks_files = filter file_accesses where (
file_path CONTAINS "\\Windows\\System32\\Tasks" OR
file_path CONTAINS "\\Windows\\Tasks"
)
output schtasks_processes, schtasks_files

Splunk Query (Production Implementation):
Provided ready-to-use SPL syntax for Splunk environments
LogPoint Search:
Alternative implementation for LogPoint SIEM
Why This Matters:
CAR bridges the gap between knowing adversary techniques exist and actually detecting them. Instead of reading “adversaries use scheduled tasks” and wondering how to find that activity, analysts get concrete detection logic they can implement immediately.
Connection to My Research Background:
This structured approach to detection development mirrors academic research methodology: hypothesis (adversaries use this technique) → operationalization (how do we measure it?) → validation (does this query actually detect the behavior?). My quantitative research training directly applies to developing and validating detection analytics.

Defensive Framework - D3FEND

What D3FEND Provides:
While ATT&CK describes how attackers operate, D3FEND describes how defenders stop them. It’s the defensive counterpart to offensive tactics.
D3FEND Matrix Structure (7 Tactics):
1. Model - Understanding the system and threats
2. Harden - Strengthening defenses
3. Detect - Identifying malicious activity
4. Isolate - Containing threats
5. Deceive - Misleading attackers
6. Evict - Removing threats
7. Restore - Recovering from incidents
Example Technique - Credential Rotation (D3-CRO):
Definition: Regularly changing passwords to prevent credential reuse attacks
How It Works:
∙ Invalidates stolen credentials through scheduled rotation
∙ Reduces window of opportunity for credential-based attacks
∙ Forces adversaries to re-compromise credentials repeatedly
Digital Artifact Relationships:
D3FEND maps defensive techniques to specific artifacts (files, processes, network connections), showing exactly what each technique protects.
ATT&CK Relationships:
Links defensive techniques to the offensive techniques they mitigate, enabling defenders to prioritize controls based on relevant threats.
Intelligence Application:
When analyzing threat reports mentioning credential theft, I can immediately reference D3FEND to identify appropriate countermeasures. This creates a direct link between threat intelligence and defensive action.

Additional MITRE Resources
Adversary Emulation Library
Purpose: Step-by-step guides for mimicking specific threat groups.  
Maintained by: Center for Threat Informed Defense (CTID)Value: Enables realistic red team exercises based on actual adversary behavior
Use Case for Threat Intelligence:
When reporting on a specific APT group, analysts can reference available emulation plans to help red teams validate whether organizational defenses can detect that group’s TTPs.

Caldera - Automated Adversary Emulation
What it is: Automated tool for simulating attacker behavior.  
How it works: Uses ATT&CK framework to execute realistic attack sequences.  
Applications:
∙ Red team exercises
∙ Purple team collaboration
∙ Detection validation
∙ Incident response training
Intelligence Integration:
Caldera can execute emulation plans based on threat intelligence reports, enabling organizations to test whether they can detect the specific adversary TTPs identified through intelligence analysis.

Emerging Frameworks
AADAPT (Adversarial Actions in Digital Asset Payment Technologies):
∙ Focuses on blockchain, smart contracts, digital wallets
∙ Threat landscape for cryptocurrency and digital asset systems
∙ Emerging threat area as organizations adopt blockchain technology
ATLAS (Adversarial Threat Landscape for AI Systems):
∙ Threats targeting AI/ML systems
∙ Attack techniques specific to machine learning models
∙ Critical as AI adoption accelerates across security operations
Why These Matter:
As threat intelligence analysts, we need to track emerging attack surfaces. These frameworks provide structured approaches to understanding threats in new technology domains.

Key Takeaways
Technical Skills Developed:
∙ Proficiency with MITRE ATT&CK framework structure and navigation
∙ Ability to map threat intelligence to structured TTPs
∙ Understanding of detection analytics development via CAR
∙ Knowledge of defensive countermeasures through D3FEND
∙ Familiarity with adversary emulation resources and methodologies
Operational Insights:
∙ How threat intelligence professionals translate raw data into actionable intelligence
∙ The importance of common language for cross-organizational security communication
∙ How frameworks bridge the gap between threat reports and defensive implementation
∙ Why structured approaches enable pattern recognition across disparate incidents
∙ How research methodology (my academic background) applies to threat analysis workflows
Connection to Threat Intelligence Analyst Role:
This training addresses core competencies required for threat intelligence positions:
∙ MITRE ATT&CK expertise - Industry-standard framework proficiency
∙ Threat actor profiling - Analyzing groups using structured methodologies
∙ Detection development - Translating intelligence into actionable detections
∙ Defensive strategy - Understanding countermeasures for identified threats
∙ Communication - Using common language to share intelligence effectively

Real-World Application
How I would apply this in a threat intelligence analyst role:

Scenario 1: Analyzing New Threat Report
When a vendor publishes research on a new campaign, I would:
1. Extract IOCs and observed behaviors
2. Map behaviors to ATT&CK techniques
3. Check CAR for existing detection analytics
4. Identify detection gaps and develop new analytics
5. Reference D3FEND for mitigation recommendations
6. Communicate findings using ATT&CK IDs for clarity
   
Scenario 2: Threat Group Profiling
When tasked with profiling an APT group relevant to our sector:
1. Research group’s historical activity in ATT&CK Groups database
2. Use Navigator to visualize their TTP patterns
3. Analyze which techniques are most frequently used
4. Assess our detection coverage against their preferred methods
5. Prioritize detection/mitigation efforts based on group’s likely approach
6. Brief stakeholders using structured ATT&CK framework
   
Scenario 3: Detection Engineering
When developing new detection rules:
1. Start with ATT&CK technique we want to detect
2. Review CAR for existing analytics and implementation guidance
3. Adapt pseudocode logic to our SIEM platform
4. Validate detection using Caldera emulation (if available)
5. Document detection mapped to ATT&CK technique ID
6. Track coverage using Navigator matrix

Portfolio Integration
This MITRE framework analysis serves as the foundation for my threat intelligence research portfolio. All subsequent threat analysis work will reference ATT&CK techniques, enabling:
∙ Consistent Terminology: All threat reports use standardized ATT&CK IDs
∙ Detection Mapping: Portfolio projects show detection coverage using Navigator
∙ Framework Fluency: Demonstrates ability to operate within industry-standard frameworks
∙ Analytical Rigor: Shows systematic approach to threat analysis using established methodologies
Combined with my quantitative research background and statistical analysis training, MITRE framework proficiency positions me to conduct rigorous, structured threat intelligence research using industry-standard methodologies.

Resources
∙ TryHackMe Room: MITRE
∙ MITRE ATT&CK: attack.mitre.org
∙ ATT&CK Navigator: mitre-attack.github.io/attack-navigator
∙ Cyber Analytics Repository: car.mitre.org
∙ D3FEND: d3fend.mitre.org

STATUS: COMPLETED ✅
Next Rooms:
∙ MISP (Threat Intelligence Platform)
∙ OpenCTI (Investigative Scenarios)
∙ Threat Intelligence Tools

This documentation demonstrates comprehensive understanding of the threat intelligence industry’s foundational frameworks and methodologies - essential capabilities for threat intelligence analyst roles.

