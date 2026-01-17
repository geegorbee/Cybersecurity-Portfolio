# SOC 2 Control Mapping Framework

**Translating compliance frameworks into operational evidence**

---

## Overview

This control mapping demonstrates how SOC 2 Trust Service Criteria translate into technical evidence sources and collection procedures. Built to show understanding of framework-to-operations translation for GRC compliance roles.

**Purpose:**
- Map SOC 2 controls to evidence sources
- Define collection methods and frequency
- Demonstrate framework knowledge
- Show operational compliance thinking

---

## What's Inside

### [Control Mapping Document](./control-mapping.md)

Comprehensive mapping of key SOC 2 controls including:

**CC6: Logical and Physical Access Controls**
- User access reviews
- RBAC configuration
- Access provisioning/deprovisioning
- Cloud service access management

**CC7: System Operations & Monitoring**
- SIEM monitoring
- Anomaly detection
- Incident response procedures
- System availability monitoring

**CC8: Change Management**
- Change approval processes
- Testing validation
- Deployment controls

**CC9: Risk Assessment**
- Risk identification
- Risk register maintenance
- Control impact analysis

---

## Framework Translation

### SOC 2 ↔ NIST 800-53 Crosswalk

Understanding multi-framework environments:

| SOC 2 Category | NIST 800-53 Family | Focus Area |
|----------------|-------------------|------------|
| CC6 (Access) | AC (Access Control) | Authentication, RBAC, authorization |
| CC7 (Monitoring) | AU (Audit), SI (System Integrity) | Logging, monitoring, incident detection |
| CC8 (Change) | CM (Configuration Management) | Change control, baselines |
| CC9 (Risk) | RA (Risk Assessment) | Risk identification, assessment |

**Why this matters:**
- Organizations often need multiple certifications (SOC 2 + ISO 27001 + FedRAMP)
- Same evidence can satisfy multiple frameworks with proper mapping
- Efficient compliance programs leverage framework overlap

---

## Real-World Application

### Evidence Collection Strategy

For each control, the mapping identifies:

1. **Evidence Type**  
   What artifact proves control effectiveness? (logs, tickets, reports)

2. **Source System**  
   Where does evidence come from? (AWS IAM, Splunk, Jira)

3. **Collection Method**  
   How is it gathered? (API query, manual export, automated script)

4. **Frequency**  
   How often? (continuous, quarterly, per-event)

### Operational Context

Maps controls to real operational experience:

- **CRA IAM Operations:** Access management for 100+ users
- **AWS Connect:** Cloud service access provisioning (2022-2024)
- **Audit Support:** Evidence documentation for federal compliance
- **RBAC Enforcement:** Least-privilege and segregation of duties

---

## Use Cases

### For GRC Analysts
- Understand control-to-evidence relationships
- Plan evidence collection workflows
- Identify automation opportunities

### For Auditors
- Quickly locate relevant evidence sources
- Validate control implementation
- Cross-reference frameworks

### For Security Engineers
- Design technical controls that satisfy compliance
- Automate evidence collection
- Build compliance into operations

---

## Related Work

**Portfolio Projects:**
- [Evidence Automation](../Evidence-Automation/) - Python script demonstrating automated collection
- [PwC GRC Internship](../../Virtual-Internships/PwC-Cyber/) - SOX controls and risk assessment
- [Deloitte Technology Internship](../../Virtual-Internships/Deloitte-Technology/) - Cyber consulting scenarios

**Skills Demonstrated:**
- Framework knowledge (SOC 2, NIST, ISO concepts)
- Evidence identification and mapping
- Operational security thinking
- Multi-framework translation

---

## About This Work

Created to demonstrate GRC operational understanding for compliance-focused security roles. Shows ability to translate abstract framework requirements into concrete technical evidence and operational procedures.

**Target Roles:**
- GRC Analyst/Engineer
- Compliance Automation Engineer  
- Risk Analyst
- Security Operations (compliance focus)

---

## Contact

**Author:** Gerald Brown  
**Email:** gerald.brown@alumni.utoronto.ca  
**LinkedIn:** [linkedin.com/in/gerald-brown-63168223a](https://linkedin.com/in/gerald-brown-63168223a)  
**Portfolio:** [github.com/geegorbee/Cybersecurity-Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)

---

*Last Updated: January 2026*

