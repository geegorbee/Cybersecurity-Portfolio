Certification: Qualys Vulnerability Management Foundation

Issuer: Qualys

Completed: 2025

Link to Certificate: (Add your GitHub PDF URL here)

🎯 Overview


The Qualys Vulnerability Management Foundation course provides practical training on how organizations identify, prioritize, and remediate security vulnerabilities across their assets. It teaches both the technical process (scanning, evaluating findings) and the operational workflow (prioritization, remediation, verification).

This aligns directly with real-world security team responsibilities in SOC, GRC, Cloud Security, and IT Risk Management.

🔑 Key Concepts & Takeaways


1. Vulnerability Management Lifecycle

The end-to-end phases covered:

Asset Discovery – identifying systems, hosts, and services

Scanning – running authenticated/unauthenticated scans

Analysis – interpreting results

Prioritization – determining what needs fixing first

Remediation – patching, configuration changes

Verification – rescanning to confirm closure

Reporting – dashboards, executive summaries

This lifecycle maps directly to NIST SP 800-40 and NIST CSF (ID.AM, PR.IP, DE.CM).


2. Understanding CVEs, CVSS, and QIDs
CVE (Common Vulnerabilities and Exposures): unique ID for vulnerabilities

CVSS (Common Vulnerability Scoring System): industry-standard scoring

Qualys QID: Qualys’s internal ID linking to detection logic and remediation guidance

Why this matters:

Qualys QIDs include step-by-step fix instructions, detection logic, and references — essential for SOC & IT Ops collaboration.


3. Prioritization Beyond CVSS: Real-World Ranking

The training emphasized that CVSS alone is not enough.

True risk prioritization requires three things:


🔹 1. Severity (CVSS)

Critical, High, Medium, Low.


🔹 2. Asset Criticality

Is the system:

Public-facing?

A domain controller?

A database server?

A production asset?



🔹 3. Threat Intelligence Signals (EPSS, known exploits)


EPSS ≈ Exploit Prediction Scoring System

This predicts how likely a CVE is to be exploited in the next 30 days.

High CVSS + High EPSS + Critical Asset = P1 remediation.

4. Authenticated vs Unauthenticated Scans
Authenticated scans = far more accurate, deeper visibility.

Unauthenticated scans = external perspective, good for perimeter assessment.


This distinction matters during interviews — many juniors don’t know the difference.


5. Patch & Configuration Management

Qualys reinforces that VM is not just about patching:

Misconfigurations

Weak services

Deprecated protocols

Missing registry settings

Legacy software


These often pose greater risk than unpatched software.


6. Validation & Reporting


Proper workflow includes:

Creating tickets for IT

Tracking remediation SLAs

Rescanning after changes

Producing executive dashboards

Documenting false positives or mitigations

These reporting skills align perfectly with GRC, SOC Tier 1, and Risk Analyst roles.


🛠 Tools & Techniques Learned
Navigating Qualys dashboards

Launching on-demand and scheduled scans

Understanding scan results and QIDs

Filtering results by:

Host

Operating system

Severity

Exploitability

Remediation workflows

Creating asset groups


🧩 How This Applies to Real Security Roles

SOC Analyst
Monitor vuln feeds associated with active threats

Escalate high-risk vulnerabilities during incidents


GRC Analyst
Document vuln mgmt policies, risk ratings, and audit evidence

Track compliance with remediation SLAs

Support assessments (NIST, ISO, CIS Controls)


Cloud Security Analyst
Integrate VM into cloud environments (Azure, AWS)

Harden images and enforce secure baselines


Cybersecurity Analyst (Generalist)
Communicate remediation requirements to IT teams

Build prioritization matrices

Produce executive summaries


📌 Summary

This course strengthened my understanding of:

How enterprise VM programs operate

How qualitative and quantitative risk scores combine

Why vuln management is core to both SOC and GRC

How to communicate findings for remediation



These skills directly support my progression toward:

SOC Tier 1 Analyst

Vulnerability Analyst

GRC Analyst

IAM/Cyber Support roles
