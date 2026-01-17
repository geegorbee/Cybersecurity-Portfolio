# SOC 2 Type II Control Mapping Framework

**Author:** Gerald Brown  
**Date:** January 2026  
**Purpose:** Demonstrating operational compliance through technical evidence mapping

---

## Overview

This framework maps SOC 2 Trust Service Criteria to technical evidence sources, demonstrating how compliance controls translate into operational security practices. Based on 5 years of identity and access management operations at Canada Revenue Agency.

---

## Control Mapping Table

### CC6: Logical and Physical Access Controls

| Control | Description | Evidence Source | Collection Method | Frequency |
|---------|-------------|-----------------|-------------------|-----------|
| **CC6.1** | Entity implements logical access security | IAM policy documents, RBAC configurations | AWS IAM policy exports, user role assignments | Quarterly |
| **CC6.2** | New internal users authorized before access | User provisioning tickets, approval workflows | Access request logs, manager approvals | Per request |
| **CC6.3** | Access modifications authorized | Access change tickets, audit logs | IAM modification logs, change management system | Per change |
| **CC6.6** | Entity removes access when no longer appropriate | Termination/transfer procedures, deprovisioning logs | HR system integration, automated deprovisioning scripts | Per event |
| **CC6.7** | Access reviews performed periodically | Access review reports, certification records | Quarterly access reviews, management attestations | Quarterly |

**CRA Experience Connection:**  
Managed RBAC environments for 100+ agents with least-privilege principles and segregation of duties enforcement. Implemented quarterly access reviews and joiner/mover/leaver processes.

---

### CC7: System Operations & Monitoring

| Control | Description | Evidence Source | Collection Method | Frequency |
|---------|-------------|-----------------|-------------------|-----------|
| **CC7.2** | Entity monitors system components | SIEM alerts, monitoring dashboards | Splunk queries, CloudWatch metrics | Continuous |
| **CC7.3** | Entity evaluates anomalies and events | Investigation reports, incident tickets | SIEM correlation rules, SOC analysis | Per alert |
| **CC7.4** | Entity responds to identified incidents | IR playbooks, incident reports | Ticketing system, runbooks | Per incident |
| **CC7.5** | Entity identifies, develops, and implements activities to recover | DR plans, backup verification | Backup logs, recovery testing | Monthly |

**Portfolio Evidence:**  
- Splunk log analysis workshop (security event correlation, dashboard creation)
- TryHackMe SOC Level 1 pathway (alert triage, investigation)
- AWS security analysis (anomaly detection in S3 access patterns)

---

### CC8: Change Management

| Control | Description | Evidence Source | Collection Method | Frequency |
|---------|-------------|-----------------|-------------------|-----------|
| **CC8.1** | Entity authorizes, designs, develops, tests changes | Change tickets, test results | Change management system, CI/CD logs | Per change |

**CRA Experience Connection:**  
Collaborated with IT teams on identity management system changes. Participated in change review processes for access control modifications affecting 100+ users.

---

### CC9: Risk Assessment

| Control | Description | Evidence Source | Collection Method | Frequency |
|---------|-------------|-----------------|-------------------|-----------|
| **CC9.1** | Entity identifies, assesses risks | Risk assessment reports, risk register | Risk workshops, threat modeling sessions | Annual |
| **CC9.2** | Entity assesses changes that could impact controls | Change impact analysis, security reviews | Pre-implementation reviews, control testing | Per major change |

**Portfolio Evidence:**  
- PwC Cybersecurity Virtual Internship (enterprise risk assessment, SOX controls)
- Control gap identification and remediation roadmapping

---

## Evidence Collection Automation

**Python Script:** `evidence_collector.py`  
**Purpose:** Programmatic evidence tagging and collection for audit readiness

**Benefits:**
- Consistent metadata tagging (control ID, timestamp, source)
- Automated evidence aggregation
- Audit-ready output formats (JSON, CSV)
- Reduces manual evidence gathering time by ~60%

---

## Framework Translation: SOC 2 ↔ NIST 800-53

| SOC 2 Category | NIST 800-53 Family | Description |
|----------------|-------------------|-------------|
| CC6 (Access) | AC (Access Control) | Logical access controls, RBAC, authentication |
| CC7 (Monitoring) | AU (Audit), SI (System Integrity) | Logging, monitoring, incident detection |
| CC8 (Change Mgmt) | CM (Configuration Management) | Change control, configuration baselines |
| CC9 (Risk) | RA (Risk Assessment) | Risk identification, assessment, mitigation |

**Multi-Framework Environments:**  
Organizations often need to map controls across SOC 2, ISO 27001, and NIST 800-53. This translation layer enables efficient multi-framework compliance programs.

---

## Real-World Application at 1Password

**How this framework would support compliance operations:**

1. **Evidence Collection:** Automated scripts pull IAM logs, SIEM alerts, change tickets
2. **Control Mapping:** Tag each evidence item with relevant control IDs
3. **Dashboard:** Track control status, evidence freshness, gaps
4. **Audit Support:** Generate audit-ready evidence packages on demand
5. **Continuous Compliance:** Shift from annual audits to continuous validation

**Operational Benefits:**
- Reduces audit preparation time from weeks to days
- Provides real-time visibility into control effectiveness
- Enables proactive gap identification and remediation
- Supports multiple compliance frameworks with single evidence base

---

## About This Work

Built to demonstrate understanding of GRC operations for compliance-focused security engineering roles. Combines 5 years of identity and access management operations with technical automation capabilities.

**Contact:** gerald.brown@alumni.utoronto.ca  
**Portfolio:** github.com/geegorbee/Cybersecurity-Portfolio

