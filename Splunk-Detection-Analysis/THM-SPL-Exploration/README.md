SPLUNK: EXPLORING SPL - HANDS-ON LAB
TryHackMe Room | Completed: January 27, 2026 | Difficulty: Easy

Overview
I completed TryHackMe’s “Splunk: Exploring SPL” room to build practical Search Processing Language (SPL) query skills - the core query language used by SOC analysts to investigate security events in Splunk SIEM. This lab covered filtering techniques, transformational commands, and data manipulation essential for alert triage and threat hunting.
SPL is what makes Splunk powerful for security operations. Understanding how to construct effective queries, chain commands together, and extract meaningful insights from log data is fundamental to SOC analyst work. This room built directly on the architecture fundamentals from “Splunk: The Basics” and put that knowledge into practical application.

Learning Objectives:

Through this lab, I gained hands-on experience with:
∙ Search Processing Language (SPL) Fundamentals: Understanding how to construct queries using operators, filters, and commands
∙ Filtering Techniques: Narrowing search results to focus on relevant security events
∙ Transformational Commands: Converting raw log data into structured, analyzable formats
∙ Data Manipulation: Sorting, ordering, and organizing results for effective investigation
∙ Statistical Analysis: Using stats commands to identify patterns and anomalies

Key SPL Components

1. Search Field Operators
I learned how to use comparison operators, boolean logic, and wildcards to filter security events - essential skills for alert triage.
Comparison Operators:
Working through Windows event logs, I practiced filtering based on specific conditions:

index=windowslogs AccountName!=SYSTEM

This query excludes system-generated events to focus on user activity - exactly what I’d do when investigating potential insider threats or compromised user accounts. Understanding comparison operators (=, !=, <, >, <=, >=) enables precise filtering of security data.
Boolean Operators (AND, OR, NOT):
I practiced combining multiple conditions to narrow investigation scope:

index=windowslogs AccountName!=SYSTEM AND AccountName=James

This multi-condition filtering is critical for SOC work - when investigating a specific user account during an incident, I need to exclude noise (system events) while focusing on targeted activity (James’s actions).
Wildcards:
Practiced using wildcards for pattern matching across IP addresses:

index=windowslogs DestinationIp=172.*

This technique is valuable for investigating activity within specific network segments (e.g., all internal 172.x.x.x addresses) or identifying lateral movement patterns during incident response.
Connection to My Experience: These filtering techniques directly apply to the triage work I performed at CRA - identifying anomalous access patterns, filtering out legitimate system activity, and focusing investigations on suspicious user behavior.


2. Filtering Commands
I practiced SPL commands that refine search results for focused investigation:
fields - Displaying Relevant Data:

index=windowslogs | fields + host + User + SourceIp

In real SOC investigations, analysts don’t need to see every field - just the ones relevant to the current investigation. This command lets me create focused views showing only hostname, user, and source IP when investigating authentication events.
search - Chaining Searches:

index=windowslogs | search Powershell

The pipe (|) operator chains commands together, enabling progressive filtering. This query first pulls all Windows logs, then filters for PowerShell activity - critical for detecting fileless malware and living-off-the-land attacks.
dedup - Removing Duplicates:

index=windowslogs | table EventID User Image Hostname | dedup EventID

High-volume environments generate repetitive events. This command shows unique Event IDs, helping identify distinct security events rather than thousands of duplicate entries. Essential for understanding scope during investigations.
rename - Improving Clarity:

index=windowslogs | fields + host + User + SourceIp | rename User as Employees

This command improves report readability by renaming generic field names to more descriptive ones - useful when presenting findings to management or creating dashboards.


3. Structuring Search Results
I learned commands that organize investigation results for analysis:
table - Creating Focused Views:

index=windowslogs | table EventID Hostname SourceName

The table command creates structured output with only specified columns - exactly what’s needed when documenting incidents or creating investigation timelines.
head and tail - Sampling Data:

index=windowslogs | table _time EventID Hostname SourceName | head 5
index=windowslogs | table _time EventID Hostname SourceName | tail 5

These commands show the first or last N results - useful for spot-checking data quality, identifying patterns at beginning/end of timeframes, or quickly sampling large datasets.
sort - Ordering Results:

index=windowslogs | table _time EventID Hostname SourceName | sort Hostname

Sorting enables pattern recognition - grouping events by hostname reveals which systems are most active, sorting by time shows chronological attack progression.
reverse - Changing Order:

index=windowslogs | table _time EventID Hostname SourceName | reverse

Simple but powerful - reversing chronological order can reveal patterns not obvious in default sorting.


4. Transformational Commands
I practiced commands that convert raw logs into actionable intelligence:
top - Identifying Frequent Events:

index=windowslogs | top limit=7 Image

This shows the most common processes executed - critical for establishing baselines and spotting anomalies. If a process suddenly appears in top 7 that shouldn’t be there, it warrants investigation.
rare - Finding Unusual Activity:

index=windowslogs | rare limit=7 Image

The opposite of top - shows least common processes. This is powerful for threat hunting - rare processes often indicate malicious activity, unauthorized software, or initial compromise.
highlight - Visual Investigation:

index=windowslogs | highlight User, host, EventID, Image

Highlighting fields in raw logs makes visual pattern recognition easier during manual investigation - helps spot IOCs quickly when reviewing event details.


5. Statistical Analysis (STATS Commands)
I learned how to use statistical functions for anomaly detection and trend analysis:
Available STATS functions:
∙ avg() - Calculate averages (e.g., average authentication failures per user)
∙ max() / min() - Find maximum/minimum values (e.g., highest outbound traffic volume)
∙ sum() - Calculate totals (e.g., total failed login attempts)
∙ count() - Count occurrences (e.g., number of PowerShell executions per host)
These statistical operations enable baseline establishment and deviation detection - foundational concepts for behavioral-based threat detection.


6. Chart Commands (Visualization)
I practiced transforming data into visual representations:
chart - Creating Data Visualizations:

index=windowslogs | chart count by User

This creates a chart showing event counts per user - visual representation makes patterns obvious that might be missed in text data. Essential for executive reporting and dashboard creation.
timechart - Time-Series Analysis:

index=windowslogs | timechart count by Image

Time-series charts show how activity changes over time - critical for identifying attack timelines, detecting beaconing behavior, or spotting unusual activity during off-hours.


Practical Investigation Workflow
Through these exercises, I developed a systematic approach to log investigation:

1. Broad Search → Narrow Focus:
∙ Start with index and basic criteria (index=windowslogs)
∙ Apply filters to remove noise (AccountName!=SYSTEM)
∙ Add conditions to focus on specific activity (AND SourceIp=172.*)

2. Structure the Data:
∙ Create tables with relevant fields (| table _time User SourceIp DestinationIp)
∙ Sort by relevant criteria (| sort _time)
∙ Limit to manageable results (| head 20)

3. Identify Patterns:
∙ Find most/least common occurrences (| top / | rare)
∙ Apply statistical analysis (| stats count by User)
∙ Visualize trends (| timechart count by Hostname)

4. Document Findings:
∙ Rename fields for clarity (| rename User as AccountName)
∙ Create focused views for reporting (| fields + _time + User + EventID)
This workflow mirrors how I approached investigations at CRA - starting broad, applying filters to reduce noise, identifying patterns, and documenting findings.


Key Takeaways
Technical Skills Developed:
∙ Hands-on SPL query construction using operators, filters, and commands
∙ Ability to chain multiple commands for progressive data refinement
∙ Understanding of transformational commands for data analysis
∙ Statistical and visualization capabilities for pattern recognition
∙ Systematic investigation methodology using structured queries
Operational Insights:
∙ The importance of filtering to reduce noise in high-volume environments
∙ How statistical analysis reveals baselines and anomalies
∙ Why visualization accelerates pattern recognition and executive communication
∙ How command chaining enables complex investigations with simple building blocks
Connection to SOC Work:
These SPL skills directly enable SOC Tier 1 responsibilities:
∙ Alert Triage: Quickly filter alerts to assess severity and scope
∙ Investigation: Chain commands to follow evidence trails and identify IOCs
∙ Pattern Recognition: Use stats and charts to spot anomalies in normal activity
∙ Documentation: Create structured tables and reports for escalation to Tier 2
∙ Threat Hunting: Proactively search for rare/unusual activity indicating compromise

Real-World Application
How I would apply these skills in a SOC analyst role:
Scenario: Investigating Suspicious Authentication Activity

index=windowslogs EventCode=4625
| stats count by User, SourceIp
| where count > 5
| sort -count

This query identifies users with multiple failed login attempts (EventCode 4625), groups by user and source IP, filters for more than 5 failures, and sorts by frequency - classic brute force attack detection.
Scenario: Hunting for PowerShell Lateral Movement

index=windowslogs Image="*powershell.exe"
| search "Invoke-Command" OR "Enter-PSSession"
| table _time User ComputerName CommandLine
| sort _time

This detects PowerShell remoting activity that could indicate lateral movement during an active breach.
Scenario: Baseline Analysis for Anomaly Detection

index=windowslogs
| timechart span=1h count by User
| where count > 100

This creates hourly activity baselines per user, highlighting periods of abnormally high activity that warrant investigation.

Next Steps
This SPL foundation prepares me for advanced Splunk work:
∙ Investigating with Splunk - Apply these query skills to real security investigations
∙ Advanced SPL - Correlation searches, subsearches, lookups, and complex detection logic
∙ Splunk Enterprise Security - Using SPL within Enterprise Security app for production SOC work
My goal is to demonstrate not just theoretical SPL knowledge, but practical investigation capabilities using queries I’ve written and documented - skills directly applicable to SOC analyst positions.

Resources
∙ TryHackMe Room: Splunk: Exploring SPL
∙ Splunk SPL Documentation: Search Reference

STATUS: COMPLETED ✅
Previous Room: Splunk: The Basics
Next Room: Investigating with Splunk

