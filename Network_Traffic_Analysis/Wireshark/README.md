Network Traffic Analysis - Wireshark Basics
Overview
I completed hands-on training in network packet analysis using Wireshark, the industry-standard open-source packet analyzer used by security operations centers, incident responders, and network engineers worldwide. This training provided foundational skills in capturing, inspecting, and filtering network traffic at the packet level - a critical capability for investigating security incidents, detecting anomalies, and understanding network-based attacks.
While log analysis (like my Splunk investigations) provides event-level visibility, packet analysis offers the deepest level of network forensics: examining the raw bytes traveling across the wire. This granular view enables detection of sophisticated attacks that evade log-based detection, reconstruction of attacker command-and-control sessions, and extraction of malicious files from network traffic.
Note: This is the foundation of an ongoing network analysis portfolio. As I progress through TryHackMe's Security 101 (SEC1) and Network Traffic Analysis pathways, I will expand this with tcpdump command-line analysis, nmap reconnaissance detection, and advanced protocol analysis scenarios.

Learning Objectives
Through this hands-on lab, I developed capabilities in:
Packet Capture & Analysis Fundamentals:

Navigating Wireshark's interface and packet inspection panes
Loading and analyzing PCAP (packet capture) files
Understanding packet structure across OSI model layers
Interpreting hex and ASCII packet representations

Protocol Analysis:

Dissecting packets to examine Frame, Ethernet, IP, TCP/UDP, and Application layers
Understanding protocol-specific fields (TCP flags, HTTP headers, DNS queries)
Identifying normal vs. suspicious protocol behavior
Analyzing protocol errors and reassembly issues

Traffic Filtering & Investigation:

Applying display filters to isolate traffic of interest
Using conversation filters to track communication sessions
Following TCP/UDP/HTTP streams to reconstruct application data
Filtering by protocol, port, IP address, and packet content

Incident Response Workflows:

Marking packets of interest during investigation
Adding analyst comments for collaboration
Exporting suspicious packets for deeper analysis
Extracting files transferred over network protocols (HTTP, SMB, FTP)


Core Wireshark Capabilities
Packet Dissection - OSI Layer Breakdown
Wireshark decodes network traffic across all seven OSI layers, revealing:
Layer 1 - Frame/Physical:

Packet arrival time and capture interface
Frame number (for investigation tracking)
Frame length and capture length
Encapsulation type

Layer 2 - Data Link (Ethernet):

Source and destination MAC addresses
Ethernet frame type (IPv4, IPv6, ARP)
VLAN tagging (if present)

Layer 3 - Network (IP):

Source and destination IP addresses
IP version, header length, TTL (Time To Live)
Fragmentation flags and identification
Protocol indicator (TCP, UDP, ICMP)

Layer 4 - Transport (TCP/UDP):

Source and destination ports
TCP flags (SYN, ACK, PSH, RST, FIN)
Sequence and acknowledgment numbers
Window size and TCP options
UDP datagram structure

Layer 5-7 - Application:

Protocol-specific data (HTTP, DNS, SMTP, FTP, SMB)
Request/response content
Headers, payloads, and data transfers

Practical Application:
This layered approach enables targeted investigation. For example, when investigating lateral movement, I can:

Filter Layer 3 (IP) for internal source/destination pairs
Examine Layer 4 (TCP) for port patterns (445 for SMB, 3389 for RDP)
Analyze Layer 7 (SMB) for authentication attempts and file transfers

Traffic Filtering Techniques
Display Filters - Basic Queries:
I practiced fundamental filtering operations:
Protocol Filtering:
- http (show only HTTP traffic)
- dns (show only DNS queries/responses)
- tcp (show only TCP traffic)
- arp (show only ARP requests/responses)

Port Filtering:
- tcp.port == 80 (HTTP traffic)
- tcp.port == 443 (HTTPS traffic)
- tcp.port == 445 (SMB file sharing)
- udp.port == 53 (DNS queries)

IP Address Filtering:
- ip.addr == 192.168.1.100 (any traffic to/from this IP)
- ip.src == 10.0.0.5 (traffic originating from this IP)
- ip.dst == 172.16.0.10 (traffic destined for this IP)
Advanced Filtering - Logical Operators:
Combining filters for complex investigations:
AND Logic:
- http and ip.addr == 192.168.1.50
  (HTTP traffic specifically involving this IP)

OR Logic:
- tcp.port == 80 or tcp.port == 443
  (Web traffic on both HTTP and HTTPS ports)

NOT Logic:
- !arp
  (Everything except ARP traffic)

Nested Logic:
- (tcp.port == 445 or tcp.port == 139) and ip.src == 192.168.1.0/24
  (SMB traffic from internal subnet)
Right-Click Menu Shortcuts:
Rather than manually typing filters, Wireshark enables point-and-click filtering:

Apply as Filter: Instantly filter for the clicked value
Prepare as Filter: Add filter to bar without executing (allows combining with AND/OR)
Conversation Filter: Show all packets in this bidirectional communication
Colorize Conversation: Highlight related packets without filtering

This "if you can click it, you can filter it" approach accelerates investigation workflows.
Stream Reconstruction
Following Protocol Streams:
One of Wireshark's most powerful features is reassembling fragmented packets into complete application-layer conversations:
TCP Stream Following:
Right-click packet → Follow → TCP Stream
This reconstructs the entire TCP session, showing:

Client requests (highlighted in red)
Server responses (highlighted in blue)
Complete data transfer in readable format

Practical Examples:
HTTP Stream Analysis:
Following an HTTP stream reveals:

HTTP request headers (User-Agent, Host, Referer)
HTTP response headers (Server, Content-Type, Set-Cookie)
Full HTML content, form submissions, API calls
Unencrypted credentials (username/password in POST data)

FTP Stream Analysis:
FTP control channel (port 21) shows:

Login credentials (USER and PASS commands in plaintext)
Directory listings (LIST command responses)
File transfer initiation (STOR and RETR commands)

SMTP Stream Analysis:
Email protocol traffic reveals:

Sender and recipient addresses
Email subject lines
Message body content (if unencrypted)
Attachment metadata

Security Analysis Value:
Stream reconstruction enables detection of:

Data exfiltration (large file uploads to external servers)
Credential theft (plaintext authentication over unencrypted protocols)
Command injection attacks (suspicious commands in HTTP parameters)
Malware C2 communication (beacon patterns and tasking commands)

File Extraction from Network Traffic
Export Objects Capability:
Wireshark can extract files transferred over supported protocols:
File → Export Objects → HTTP/SMB/TFTP/FTP
This functionality enables:

Extracting malware samples from captured traffic
Recovering documents transferred during data exfiltration
Obtaining phishing email attachments from SMTP streams
Analyzing suspicious executables downloaded via HTTP

Incident Response Application:
During malware investigation, file extraction allows:

Capture network traffic during infection
Export malicious executable from HTTP download
Calculate file hash for IOC database
Submit to sandbox for behavioral analysis
Share hash via MISP for community alerting

This connects packet analysis → malware analysis → threat intelligence sharing.

Hands-On Analysis Scenarios
HTTP Traffic Investigation
Scenario: Analyzing web traffic for suspicious activity
Filtering Approach:
Step 1: Filter for HTTP traffic
Display Filter: http

Step 2: Examine HTTP request methods
Look for: POST requests (potential form submissions, data uploads)

Step 3: Follow HTTP streams to view full requests
Right-click packet → Follow → HTTP Stream

Step 4: Search for sensitive data exposure
Edit → Find Packet → String: "password"
What This Reveals:

Websites visited (HTTP Host headers)
Search queries and form submissions
Unencrypted authentication attempts
Files downloaded from web servers
User-Agent strings (identifying client software)

Security Implications:
HTTP (unencrypted) traffic exposes:

Credentials transmitted in cleartext
Session tokens vulnerable to hijacking
Personal data visible to network eavesdroppers
Malware download sources and C2 infrastructure

DNS Query Analysis
Scenario: Investigating DNS traffic for malicious domain resolution
Filtering Approach:
Display Filter: dns

Analysis Points:
- Query types (A records for IP resolution, MX for mail, TXT for various uses)
- Queried domain names (look for suspicious/random strings)
- Response codes (NXDOMAIN indicates non-existent domains)
- Query frequency (high volume may indicate DGA malware)
Threat Detection Indicators:
DNS Tunneling:

Unusually long domain names (subdomains used for data encoding)
High volume of DNS queries to single domain
TXT record queries (commonly used for data exfiltration)

Domain Generation Algorithms (DGA):

Queries for seemingly random domain names
High NXDOMAIN response rate (failed lookups)
Pattern indicating algorithmic generation rather than human typing

C2 Infrastructure:

DNS queries to recently registered domains
Queries to domains with suspicious TLDs (.xyz, .top, etc.)
Fast-flux DNS (IP addresses changing rapidly)

TCP Flag Analysis
Scenario: Detecting reconnaissance and scanning activity
TCP Three-Way Handshake:
Normal connection establishment:

Client → Server: SYN
Server → Client: SYN-ACK
Client → Server: ACK

Suspicious TCP Patterns:
SYN Scan (Port Scanning):
Display Filter: tcp.flags.syn == 1 and tcp.flags.ack == 0

Indicator: Multiple SYN packets to different ports from single source
Meaning: Attacker probing for open ports
RST Packets (Connection Refusal):
Display Filter: tcp.flags.reset == 1

Indicator: High volume of RST responses
Meaning: Scanning closed ports or IDS/firewall blocking
FIN Scan (Stealth Scanning):
Display Filter: tcp.flags.fin == 1 and tcp.flags.syn == 0

Indicator: FIN packets without prior connection establishment
Meaning: Attempting to bypass firewall rules

Expert Information - Automated Anomaly Detection
Wireshark's Expert Info system automatically flags potential issues:
Severity Levels:
SeverityColorTypical IndicatorsErrorRedMalformed packets, checksum failures, TCP retransmissionsWarnYellowOut-of-order packets, duplicate ACKs, connection resetsNoteCyanApplication error codes, unusual protocol usageChatBlueNormal protocol operation information
Common Expert Info Categories:
Checksum Errors:

May indicate packet corruption or NAT issues
Can also indicate traffic capture on virtualized interfaces (offload enabled)

TCP Retransmissions:

High retransmission rates suggest network congestion or packet loss
May indicate denial-of-service attack or network infrastructure problems

Malformed Packets:

Protocol violations or crafted packets
Potential indicator of exploitation attempts or evasion techniques

Access Expert Info:

Status bar (lower-left corner) shows summary counts
Analyze → Expert Information for detailed breakdown

Investigation Workflow:

Load PCAP file
Check Expert Info for red/yellow flags
Click category to filter related packets
Investigate flagged packets in context of surrounding traffic


Packet Marking and Commenting
Analyst Collaboration Features:
Marking Packets:

Right-click packet → Mark/Unmark Packet
Marked packets highlighted in black for visibility
Useful for flagging IOCs during investigation
Marks lost when capture file closed (session-only)

Adding Comments:

Right-click packet → Packet Comment
Persistent comments saved within PCAP file
Enables detailed annotation for team collaboration
Comments visible in packet list pane

Use Cases:
Incident Documentation:

Mark initial compromise packet: "Initial access - phishing link clicked"
Comment C2 beacon: "CobaltStrike HTTPS beacon to 45.142.212.61:443"
Mark lateral movement: "SMB connection to DC - credential theft suspected"

Team Handoff:

Junior analyst marks suspicious packets
Comments explain observed behavior
Senior analyst reviews flagged packets with context
Investigation notes preserved for reporting


Integration with Security Operations
SIEM Correlation
Wireshark complements Splunk analysis:
Splunk Alert → Wireshark Deep Dive:

SIEM detects anomalous network connection (e.g., internal host to external IP on port 8080)
Capture PCAP of relevant timeframe
Load PCAP in Wireshark
Filter for specific IP and port: ip.addr == <suspect_ip> and tcp.port == 8080
Follow TCP stream to reconstruct full session
Determine if connection is legitimate or malicious
Extract IOCs (domains, file hashes) for MISP sharing

Example - My Splunk Investigation Enhancement:
In my "Investigating with Splunk" project, I identified suspicious PowerShell execution. With packet capture, I could:

Capture network traffic during PowerShell execution
Filter for HTTP/HTTPS connections from PowerShell process
Extract downloaded payloads using "Export Objects"
Analyze C2 beaconing patterns in packet timing
Document complete attack chain: execution → download → C2

Threat Intelligence Enrichment
Connecting Wireshark → MITRE → MISP:
Investigation Workflow:

Wireshark: Extract IOCs from packet analysis (C2 IPs, malicious domains, file hashes)
MITRE ATT&CK: Map observed techniques (T1071.001 for C2 over HTTP)
MISP: Create event with extracted IOCs, tag with ATT&CK techniques, share with community

Example - Emotet Traffic Analysis:
If analyzing Emotet network traffic:

Wireshark identifies C2 IP addresses from HTTP POST requests
Extract malware binary from HTTP download
Calculate SHA256 hash
Document in MISP event with Emotet tags
Export IOCs to firewall for blocking

This demonstrates end-to-end security workflow integrating multiple tools.

Key Takeaways
Technical Skills Developed:

Packet-level network traffic analysis and protocol dissection
Display filter creation for targeted traffic isolation
Stream reconstruction for application-layer investigation
File extraction from network protocols
TCP flag analysis for reconnaissance detection

Investigation Capabilities:

Detecting network-based attacks (scanning, exploitation, C2 communication)
Identifying data exfiltration and credential theft
Analyzing malware network behavior
Reconstructing attacker actions from packet captures

Operational Understanding:

Difference between packet analysis (Wireshark) and log analysis (Splunk)
When to use packet capture vs. flow data vs. logs
How to integrate packet analysis into incident response workflows
Importance of capturing traffic during security events


Connection to SOC Analyst Role
Wireshark Proficiency Addresses Critical SOC Competencies:
Network Forensics:

Investigating security alerts requiring packet-level detail
Reconstructing attack chains from network evidence
Validating IDS/IPS alerts through traffic inspection

Malware Analysis:

Analyzing C2 communication patterns
Extracting malicious payloads from network traffic
Identifying beaconing intervals and data exfiltration

Incident Response:

Determining scope of network-based compromise
Identifying affected systems through traffic correlation
Documenting attacker TTPs from packet captures

Threat Hunting:

Proactively searching for anomalous network behavior
Identifying unauthorized protocols or suspicious connections
Detecting lateral movement and credential abuse


Portfolio Integration
Network Traffic Analysis Complements Existing Projects:
With Splunk Investigations:

Splunk provides event-level visibility (authentication logs, process execution)
Wireshark provides packet-level detail (network connections, data transfers)
Combined: Complete investigation capability from logs to packets

With MITRE Framework:

Network-based techniques identified in Wireshark map to ATT&CK
Examples: T1071 (C2 protocols), T1048 (exfiltration), T1046 (network scanning)
ATT&CK Navigator can visualize coverage from packet analysis capabilities

With MISP Threat Intelligence:

IOCs extracted from Wireshark feed into MISP events
Network indicators (IPs, domains) shared with security community
MISP-exported IOCs imported to Wireshark as display filter lists

This integrated toolset demonstrates comprehensive security analysis capability:
Logs (Splunk) + Packets (Wireshark) + Frameworks (MITRE) + Sharing (MISP) = Complete SOC Analyst Toolkit

Next Steps in Network Analysis Learning Path
TryHackMe Security 101 (SEC1) - In Progress:

tcpdump Basics: Command-line packet capture and filtering
nmap Fundamentals: Network reconnaissance and port scanning detection

TryHackMe Network Traffic Analysis Pathway - Planned:

Advanced Wireshark filtering and analysis techniques
Protocol-specific deep dives (SMB, Kerberos, SSL/TLS)
Malware traffic analysis scenarios
Network forensics case studies

Future Portfolio Additions:
As I complete additional training, this network analysis section will expand with:

tcpdump command-line packet analysis
Detection of nmap scanning activity
Analysis of encrypted traffic metadata (SSL/TLS handshakes, certificate inspection)
Advanced C2 detection techniques


Resources

TryHackMe Room: Wireshark: The Basics
Wireshark Official Documentation: https://www.wireshark.org/docs/
Wireshark Display Filter Reference: https://www.wireshark.org/docs/dfref/
Sample PCAPs: http://malware-traffic-analysis.net/


Status: FOUNDATION COMPLETE ✅
Next Module: tcpdump Basics (TryHackMe SEC1 Pathway)
This Wireshark foundation demonstrates packet-level network analysis capabilities - essential skills for SOC analysts conducting incident investigations and threat hunting operations.
