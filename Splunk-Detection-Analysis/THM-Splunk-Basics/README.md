SPLUNK: THE BASICS - HANDS-ON LAB
TryHackMe Room | Completed: Dec, 2025 | Difficulty: Easy

Overview
I completed TryHackMe’s “Splunk: The Basics” room to build foundational hands-on experience with Splunk SIEM. This lab covered the core architecture of Splunk, interface navigation, and practical log ingestion - essential skills for SOC analyst and security operations roles.
Splunk is one of the leading SIEM (Security Information and Event Management) solutions used by organizations globally to collect, analyze, and correlate network and machine logs in real-time. Understanding how to work with Splunk is critical for threat detection, incident response, and security monitoring.

Learning Objectives
Through this lab, I gained hands-on experience with:
∙ Splunk Architecture: Understanding how Forwarders, Indexers, and Search Heads work together to process security data
∙ Interface Navigation: Exploring the Splunk UI, apps panel, search interface, and dashboard functionality
∙ Data Ingestion: Practically ingesting VPN logs into Splunk and preparing them for analysis
∙ SIEM Fundamentals: Building foundational knowledge of how SIEMs collect, normalize, and index security events

Splunk Architecture - The Three Core Components
Working through this lab, I learned how Splunk’s architecture separates data collection, processing, and analysis into three distinct components:

1. Splunk Forwarder (Data Collection Agent)
The Forwarder is a lightweight agent installed on endpoints that collects and forwards log data to the Splunk Indexer. In my federal operations experience managing 100+ remote agents, I’ve seen firsthand how critical log collection is - the Forwarder concept mirrors the monitoring agents I’ve worked with for identity and access logging.
Key data sources the Forwarder collects:
∙ Web server traffic logs
∙ Windows Event Logs, PowerShell, and Sysmon data
∙ Linux host-centric logs (syslog, auth logs)
∙ Database connection requests, responses, and errors
The Forwarder’s lightweight design ensures minimal performance impact on monitored systems - important for production environments where system resources matter.

2. Splunk Indexer (Data Processing Engine)
The Indexer is where the heavy lifting happens. It receives raw log data from Forwarders, parses it, normalizes it into field-value pairs, and stores events in indexed format for fast searching.
This normalization process is critical for security operations - instead of dealing with dozens of different log formats, the Indexer creates a consistent structure that makes correlation and analysis possible. Coming from a compliance background where I’ve worked with multiple identity management systems, I appreciate how this standardization enables effective threat detection across diverse data sources.

3. Search Head (Analysis Interface)
The Search Head is where analysts interact with indexed data using SPL (Search Processing Language). This is the interface I’ll be using extensively in subsequent Splunk rooms to query logs, investigate incidents, and create detection rules.
The Search Head also provides visualization capabilities - transforming query results into charts, dashboards, and reports that communicate security findings to stakeholders. My experience briefing management on security and compliance findings translates well to this visualization and reporting capability.

Navigating the Splunk Interface
I explored the Splunk interface to understand how analysts interact with the platform daily:
Splunk Bar (Top Navigation)
∙ Messages: System-level notifications and alerts
∙ Settings: Instance configuration and administration
∙ Activity: Monitor search job progress and system processes
∙ Help: Access documentation and tutorials
∙ Find: Search across installed apps
Apps Panel
Splunk uses an app-based architecture. The default “Search & Reporting” app is where most SOC analyst work happens, but organizations can install specialized apps for different use cases (e.g., Enterprise Security, IT Service Intelligence).
Home Dashboard
By default, no dashboards are displayed on initial setup. Analysts can create custom dashboards for their specific monitoring needs - for example, failed authentication attempts, privilege escalations, or suspicious process executions. This customization capability aligns with how I’ve tailored security monitoring to specific operational needs in my CRA experience.

Practical Exercise: Ingesting VPN Logs
The hands-on portion of this lab involved uploading VPN logs to Splunk and preparing them for analysis. This five-step process mirrors real-world data onboarding workflows:
Data Ingestion Workflow:
1. Select Source
∙ Uploaded VPN log file from local system
∙ In production environments, this would typically be configured as an automated forwarding relationship
2. Select Source Type
∙ Identified log format (JSON, syslog, CSV, etc.)
∙ Proper source type selection is critical for accurate parsing - incorrect typing can result in field extraction failures
3. Input Settings
∙ Selected target index for log storage
∙ Configured hostname association for the logs
∙ Index selection matters for data retention, search performance, and access control
4. Review Configuration
∙ Verified all settings before finalizing ingestion
∙ Caught potential misconfigurations before they impact data quality
5. Complete Upload
∙ Successfully ingested VPN logs into Splunk
∙ Data immediately became searchable through the Search Head
Why This Matters
Understanding data ingestion is foundational for SOC operations. If logs aren’t ingested correctly, security events go undetected. In my CRA role managing authentication and access logs, I’ve seen how critical proper logging configuration is for audit trails and incident investigation. This lab demonstrated how Splunk handles that ingestion process at scale.

Key Takeaways
Technical Skills Developed:
∙ Hands-on experience with Splunk interface navigation
∙ Understanding of SIEM architecture (collection → processing → analysis)
∙ Practical data ingestion workflow execution
∙ Foundational knowledge for SPL query development (covered in subsequent rooms)
Operational Insights:
∙ The importance of proper data source configuration for accurate parsing
∙ How index selection impacts search performance and data organization
∙ The role of normalization in enabling cross-platform security correlation
∙ Why lightweight agent design matters for production deployments
Connection to My Experience:
This lab reinforced concepts I’ve worked with in federal security operations - log collection, data normalization for compliance reporting, and the importance of structured data for investigations. The difference is scale and automation: Splunk enables real-time correlation across thousands of endpoints, whereas my operational experience focused on smaller-scale IAM environments.

Real-World Application
How I would apply this in a SOC analyst role:
∙ Log Onboarding: When new systems need monitoring, I understand the ingestion workflow to properly configure data sources
∙ Troubleshooting: If logs aren’t appearing in Splunk, I know to check Forwarder status, Indexer processing, and source type configuration
∙ Data Quality: I can verify that logs are being parsed correctly by reviewing field extractions
∙ Collaboration: I can explain to IT teams why proper log formatting matters for security monitoring

Next Steps
This foundational lab prepares me for more advanced Splunk work:
∙ Splunk: Exploring SPL - Learn Search Processing Language for querying indexed data
∙ Investigating with Splunk - Apply SPL to real security investigations
∙ Advanced Splunk - Correlation searches, lookups, and complex detection logic
My goal is to build a complete Splunk detection portfolio demonstrating hands-on investigation and alert triage capabilities - skills directly applicable to the SOC analyst and security operations roles I’m targeting.

Resources
∙ TryHackMe Room: Splunk: The Basics
∙ Splunk Documentation: Navigating Splunk
∙ My GitHub Portfolio: Splunk Detection & Analysis

STATUS: COMPLETED ✅
Next Room: Splunk: Exploring SPL

This documentation demonstrates my commitment to building hands-on SIEM capabilities beyond just theoretical knowledge. Each room I complete adds practical skills directly applicable to security operations roles.


