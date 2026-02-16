# AWS Security Portfolio

**Focus:** Cloud security analysis, IAM security, infrastructure access control

This section documents hands-on AWS security work demonstrating practical understanding of cloud security concepts, IAM privilege analysis, and infrastructure control validation—directly applicable to GRC automation and cloud security roles.

---

## Completed Projects

### 🔒 S3cret Santa - IAM Privilege Enumeration & Role Assumption
**Completed:** December 2025 | **Lab:** TryHackMe Advent of Cyber Day 23

Performed comprehensive AWS security analysis demonstrating privilege escalation through IAM role assumption. Documented complete attack chain from initial credential compromise through data exfiltration, identified 6 critical control gaps, and provided GRC-focused remediation recommendations.

**Key Findings:**
- Privilege escalation via `sts:AssumeRole` permission
- Unencrypted S3 bucket with sensitive credentials
- Missing CloudTrail monitoring and alerting
- Overly permissive IAM policies (wildcard resources)

**Skills Demonstrated:**
- AWS CLI automation
- IAM enumeration and policy analysis
- Privilege escalation path identification
- S3 security assessment
- Control gap documentation with SOC 2/ISO 27001 mapping
- GRC automation recommendations

**[📄 View Full Security Analysis →](./S3cret-Santa/)**

---

## Skills Overview

**AWS Services:**
- Identity and Access Management (IAM)
- Security Token Service (STS)
- Simple Storage Service (S3)
- CloudTrail (logging & monitoring)

**Security Concepts:**
- IAM policy analysis and validation
- Role-based access control (RBAC)
- Privilege escalation detection
- Temporary credential management
- Cloud access control validation
- Principle of least privilege

**Automation & Scripting:**
- AWS CLI command-line automation
- Bash scripting for security testing
- Programmatic IAM enumeration
- Policy-as-code validation concepts

**GRC Application:**
- Automated control testing workflows
- Evidence collection for audits
- Compliance framework mapping (SOC 2, ISO 27001, NIST 800-53)
- Audit trail documentation
- Remediation planning

---

## Technical Highlights

### Automated IAM Risk Analysis
Demonstrated capability to script AWS CLI commands for:
- User/role/policy enumeration
- Permission analysis (direct + assumed)
- Privilege escalation path detection
- Control gap identification

### GRC Automation Examples
Applied lab findings to real-world GRC scenarios:
- Daily scans for overprivileged users
- S3 encryption compliance checks
- CloudTrail monitoring configuration
- Policy-as-code validation in CI/CD

### Security Assessment Methodology
- Reconnaissance (credential validation, IAM enumeration)
- Privilege analysis (policy review, role discovery)
- Exploitation (role assumption, resource access)
- Documentation (findings, remediation, compliance mapping)

---

## Portfolio Roadmap

**Completed:**
- ✅ AWS IAM security fundamentals
- ✅ S3 security analysis
- ✅ Privilege escalation documentation

**In Progress:**
- 🔄 Additional AWS security labs (TryHackMe)
- 🔄 Security+ certification preparation

**Planned:**
- 📋 CloudTrail SIEM analysis project
- 📋 Automated IAM risk analyzer (Python)
- 📋 Terraform security templates
- 📋 AWS Security Specialty certification

---

## Why AWS Security?

Cloud security is foundational to modern GRC roles. Organizations are migrating to AWS at scale, creating demand for professionals who understand:
- How to validate cloud security controls programmatically
- How to map AWS configurations to compliance requirements
- How to automate evidence collection for audits
- How to identify and remediate cloud misconfigurations

This portfolio demonstrates practical AWS security capabilities directly applicable to GRC automation, cloud security engineering, and compliance validation roles.

---

## Related Work

**Other Portfolio Sections:**
- [Virtual Internships](../Virtual-Internships/) - PwC Cybersecurity (GRC focus)
- [TryHackMe Projects](../TryHackMe/) - SOC analysis, Active Directory security
- [AI Portfolio](https://github.com/geegorbee/AI-Portfolio) - Berg's AI Ordering System (automation)

---

**Contact:** gerald.brown@alumni.utoronto.ca  
**LinkedIn:** [linkedin.com/in/gerald-brown-63168223a](https://linkedin.com/in/gerald-brown-63168223a)  
**GitHub:** [github.com/geegorbee](https://github.com/geegorbee)  
**Portfolio:** [Cybersecurity-Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)


