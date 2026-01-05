# PwC Cybersecurity & Controls Virtual Internship

## Comprehensive Project Analysis

**Program:** PwC Cybersecurity Consulting Job Simulation (Forage)  
**Completion:** November 2025  
**Focus Areas:** Enterprise risk assessment, SOX compliance, IT general controls, change management

**[← Back to Project Overview](./README.md)**

-----

## Table of Contents

1. [Executive Summary](#executive-summary)
1. [Project Context & Objectives](#project-context--objectives)
1. [Task 1: Procure-to-Pay Risk Assessment](#task-1-procure-to-pay-risk-assessment)
1. [Task 2: SDLC Controls Walkthrough](#task-2-sdlc-controls-walkthrough)
1. [Task 3: Change Management Control Testing](#task-3-change-management-control-testing)
1. [Task 4: Executive Findings Summary](#task-4-executive-findings-summary)
1. [Technical Skills Demonstrated](#technical-skills-demonstrated)
1. [Key Learnings & Professional Development](#key-learnings--professional-development)
1. [Tools & Frameworks Referenced](#tools--frameworks-referenced)

-----

## Executive Summary

Conducted a comprehensive cybersecurity risk assessment for MedTech Industries, a healthcare startup preparing for IPO and SOX compliance. Analyzed procure-to-pay (P2P) processes, software development lifecycle (SDLC) controls, and change management procedures across four distinct engagement tasks.

**Key Deliverables:**

- Risk analysis of financial and IT controls across three business processes
- Documentation of control design and operating effectiveness testing
- Executive summary presentation with remediation recommendations
- Formal audit walkthrough documentation

**Critical Findings:**

- **6 major control gaps** in P2P process including segregation of duties violations
- **2 control operating effectiveness failures** in change management (emergency approvals, SoD conflict)
- **1 significant SDLC gap** (missing design reviews before production deployment)

**Business Impact:** Identified critical SOX compliance gaps that would prevent successful IPO; developed 90-day remediation roadmap to achieve audit-ready state.

-----

## Project Context & Objectives

### Client Background

**MedTech Industries** is a healthcare industry startup preparing for Initial Public Offering (IPO) within the next year. As a soon-to-be public company, MedTech must comply with Sarbanes-Oxley (SOX) Act requirements, particularly Section 404 mandating effective internal controls over financial reporting.

**Challenge:** Initial leadership conversations indicated current processes and controls would likely not meet SOX requirements. The organization needed systematic assessment of control maturity and clear remediation roadmap.

### Engagement Objectives

1. **Assess current state** of key business processes and IT controls
1. **Identify control gaps** that pose risk to SOX compliance
1. **Document findings** with supporting evidence and risk assessment
1. **Provide recommendations** for remediation aligned to IPO timeline
1. **Communicate effectively** to both technical and executive stakeholders

### My Role

Acting as cybersecurity consultant working under senior associate supervision, I was responsible for:

- Analyzing client documentation against control frameworks
- Conducting stakeholder interviews and audit walkthroughs
- Performing control testing and documenting exceptions
- Synthesizing findings into executive presentations
- Developing risk-based remediation recommendations

-----

## Task 1: Procure-to-Pay Risk Assessment

**[Full Task 1 Details](./Task-1/)**

### Objective

Analyze MedTech’s Procure-to-Pay standard operating procedures, identify control gaps, and assess SOX compliance readiness.

### Methodology

- Reviewed P2P SOP documentation
- Compared processes against SOX Section 404 requirements and COSO framework
- Performed gap analysis identifying missing or insufficient controls
- Mapped process gaps to specific business risks
- Developed actionable remediation strategies

### Key Findings Summary

**Access Control & IAM Gaps:**

- Shared credentials among inventory team (eliminated accountability)
- Informal access provisioning via phone requests
- Insufficient RBAC enforcement
- No formal access request/approval workflow

**Segregation of Duties Violations:**

- Single purchasing coordinator controlling complete transaction lifecycle
- Payment authorization and processing not separated
- Invoice verification performed by operational (non-finance) teams

**Business Process Control Gaps:**

- Automated purchase requisition approvals without validation
- Missing three-way match control (PO, receipt, invoice)
- No supplier due diligence procedures
- Inadequate cash reconciliation documentation

### Impact

Identified 6 critical control gaps exposing organization to fraud risk, unauthorized transactions, and certain SOX audit failure. All gaps categorized as high or critical severity requiring remediation before IPO.

-----

## Task 2: SDLC Controls Walkthrough

**[Full Task 2 Details](./Task-2/)**

### Objective

Evaluate MedTech’s Software Development Life Cycle process for payroll system implementation against NIST standards through structured audit walkthrough.

### Methodology

- Compared client SDLC SOP to NIST SP 800-64 framework
- Prepared risk-based interview questions
- Conducted 30-minute walkthrough with time-constrained IT manager
- Documented gaps between documented procedures and leading practices

### Key Findings Summary

**Gap 1: Missing Design Reviews**

- No validation that systems meet requirements before production deployment
- Requirements accepted “at face value” without review
- **Risk:** Systems deployed that don’t meet business or security specifications

**Gap 2: Undocumented Configuration Management**

- CM activities exist but not formalized in procedures
- **Risk:** Inconsistent application; audit findings due to lack of documentation

**Gap 3: Insufficient Testing Documentation**

- Testing performed but lacks audit trail requirements
- **Risk:** Inability to demonstrate due diligence during compliance reviews

### Impact

Identified risk of deploying systems that don’t meet regulatory requirements, potentially causing costly post-implementation rework. Demonstrated effective stakeholder management under time constraints.

-----

## Task 3: Change Management Control Testing

**[Full Task 3 Details](./Task-3/)**

### Objective

Document and test change management controls for CorpLaw application, validating both design adequacy and operating effectiveness.

### Methodology

- Conducted walkthrough with IT Manager
- Documented Test of Design for two controls
- Executed Test of Operating Effectiveness through sample testing
- Documented exceptions with evidence and impact analysis

### Key Findings Summary

**Control 1.2 - Emergency Change Authorization**

- **Design:** ✅ Appropriately designed
- **Operating Effectiveness:** ❌ FAILED
- **Exception:** Emergency change approved by wrong person (requestor vs. IT Director); no CAB approval within 5-day requirement
- **Impact:** Untested changes deployed without technical oversight

**Control 1.3 - Segregation of Duties (Developer/Implementer)**

- **Design:** ✅ Appropriately designed
- **Operating Effectiveness:** ❌ FAILED
- **Exception:** User Martin France has both developer and implementer access
- **Impact:** Single individual can write and deploy code without independent review; fundamental SoD violation

### Impact

Documented 2 critical control operating effectiveness failures creating fraud risk and SOX violations. Both exceptions require immediate remediation.

-----

## Task 4: Executive Findings Summary

**[Full Task 4 Details](./Task-4/)**

### Objective

Synthesize all engagement findings into concise executive summary for Compliance Program Manager, communicating business impact and remediation priorities.

### Methodology

- Consolidated findings across all tasks
- Categorized by risk domain and severity
- Developed phased remediation roadmap
- Created one-slide executive presentation
- Prepared discussion points for stakeholder meeting

### Summary Deliverable

**Critical Findings by Domain:**

- **Financial Controls (P2P):** 3 critical, 3 high, 2 medium issues
- **Access Management:** 2 critical, 1 high issues
- **Change Management:** 2 high issues
- **SDLC Security:** 1 medium issue

**Remediation Roadmap:**

- **Phase 1 (0-30 days):** Address critical SOX blockers
- **Phase 2 (30-90 days):** Strengthen systematic controls
- **Phase 3 (90-180 days):** Implement sustainable governance

**IPO Readiness:** Currently NOT READY; achievable in 90 days with committed remediation effort.

### Impact

Provided leadership with clear understanding of compliance gaps, business risks, and actionable path to audit-ready state. Enabled informed decision-making on IPO timeline and resource allocation.

-----

## Technical Skills Demonstrated

### Governance, Risk & Compliance (GRC)

- SOX Section 404 compliance analysis and gap assessment
- Risk and Control Matrix (RCM) development
- Control design and operating effectiveness testing
- Regulatory requirements mapping (SOX, NIST, COSO frameworks)
- Audit walkthrough planning and execution
- Exception reporting with evidence documentation

### Access Control & Identity Management

- Role-based access control (RBAC) analysis
- Segregation of duties (SoD) evaluation and violation identification
- User access review and certification procedures
- Least-privilege principle application
- Access lifecycle management assessment
- Shared credential risk evaluation

### IT General Controls (ITGCs)

- Change management control testing (design and operating effectiveness)
- SDLC security control evaluation against NIST standards
- Configuration management assessment
- Emergency change authorization procedures
- Developer/implementer separation enforcement

### Risk Assessment & Analysis

- Business process risk identification and categorization
- Control gap analysis and prioritization by severity
- Risk-to-control mapping
- Remediation roadmap development with phased approach
- Business impact analysis for control failures

### Audit & Professional Services

- Test of Design (ToD) documentation
- Test of Operating Effectiveness (ToE) execution
- Structured interview techniques for audit walkthroughs
- Evidence collection and validation
- Professional audit documentation standards
- Client communication and stakeholder management

### Business & Communication Skills

- Executive-level presentation development
- Technical-to-business risk translation
- Stakeholder interview under time constraints
- Remediation planning and project phasing
- Cross-functional collaboration (IT, Finance, Compliance)

-----

## Key Learnings & Professional Development

### Technical Competencies Gained

**Control Framework Application:**

- Learned systematic approach to analyzing business processes against SOX, NIST, and COSO frameworks
- Developed ability to identify control gaps through comparison to leading practices
- Understood importance of explicitly mapping gaps to specific risks and business impacts

**Control Testing Methodology:**

- Gained hands-on experience with Test of Design vs. Test of Operating Effectiveness concepts
- Learned to distinguish between design flaws (control logic issues) and execution failures (process adherence issues)
- Understood importance of comparing actual evidence to expected control behavior
- Developed skill in documenting exceptions with clear pass/fail criteria

**Access Control & IAM:**

- Deepened understanding of segregation of duties principle and practical application
- Learned to identify SoD conflicts across different business contexts (financial, IT, development)
- Understood role of RBAC in enforcing separation through system configuration
- Recognized importance of regular access reviews and certification processes

**Change Management:**

- Learned ITIL change control principles and their application to IT systems
- Understood difference between standard, emergency, and expedited change procedures
- Recognized risks of emergency change processes and need for retrospective validation
- Saw practical examples of change approval workflow failures

### Communication & Professional Skills

**Executive Communication:**

- Learned to translate technical control failures into business risk language
- Developed ability to structure findings for non-technical audiences
- Practiced “What? So what? Now what?” presentation framework
- Understood importance of leading with business impact, not technical detail

**Stakeholder Management:**

- Gained experience conducting effective interviews with time-constrained stakeholders
- Learned to prioritize questions by risk impact when time is limited
- Developed strategies for securing follow-up when issues remain unresolved
- Understood importance of maintaining collaborative tone even when finding gaps

**Audit Walkthrough Techniques:**

- Learned value of thorough pre-meeting document review
- Developed question sequencing strategy (open-ended → targeted → probing)
- Practiced active listening to identify unstated processes or issues
- Understood when to accept responses vs. when to probe deeper

**Professional Documentation:**

- Learned industry-standard formats for control testing documentation
- Developed ability to write clear, concise findings with supporting evidence
- Understood importance of distinguishing between observations and conclusions
- Practiced balancing completeness with readability

### Risk Assessment Methodology

**Systematic Approach:**

- Learned to organize findings by risk category rather than chronological discovery
- Developed ability to assess severity based on likelihood and impact
- Understood importance of prioritizing remediation by business criticality
- Recognized value of phased remediation approach (quick wins → systematic improvements → sustainable governance)

**Root Cause Analysis:**

- Learned to look beyond symptoms to identify underlying control weaknesses
- Developed ability to distinguish between training issues, process gaps, and design flaws
- Understood how to develop recommendations that address root causes vs. symptoms

### Real-World Consulting Insights

**Pre-IPO Control Maturity:**

- Understood common control gaps in organizations transitioning from startup to regulated environment
- Learned typical timeline and effort required to establish SOX-compliant control environment
- Recognized importance of executive commitment and resource allocation to remediation

**SOX Compliance Requirements:**

- Gained practical understanding of Section 404 internal control requirements
- Learned relationship between IT General Controls and financial reporting accuracy
- Understood audit expectations for control documentation and evidence

**Control Design vs. Practice:**

- Recognized that documented controls don’t always operate as designed
- Learned importance of sampling and testing vs. relying on documented procedures
- Understood value of continuous monitoring vs. point-in-time assessments

-----

## Tools & Frameworks Referenced

### Regulatory & Compliance Standards

- **SOX (Sarbanes-Oxley Act) Section 404** - Internal control requirements for public companies
- **NIST SP 800-64 Rev. 2** - Security Considerations in the System Development Life Cycle
- **COSO Framework** - Internal Control – Integrated Framework for risk management
- **COBIT 5** - Control Objectives for Information and Related Technologies

### IT Governance & Best Practices

- **ITIL (Information Technology Infrastructure Library)** - Change management and service delivery
- **ISO 27001/27002** - Information security management systems and controls
- **CIS Controls** - Center for Internet Security cybersecurity best practices

### Audit & Control Testing

- **PCAOB Standards** - Public Company Accounting Oversight Board audit requirements
- **AICPA Audit Guides** - Professional audit methodology and documentation standards

-----

## Project Outcome & Value Delivered

### Deliverables Completed

✅ Comprehensive risk assessment across three key business processes  
✅ Documented control gaps with supporting evidence and risk categorization  
✅ Test of Design and Operating Effectiveness documentation for change management controls  
✅ Executive summary presentation with phased remediation roadmap  
✅ Professional audit documentation following industry standards

### Client Value

**Compliance Readiness:**

- Clear understanding of current SOX compliance gaps blocking IPO
- Specific remediation actions required to achieve audit-ready state
- Realistic timeline and resource requirements for control implementation

**Risk Management:**

- Identification of fraud risks and control weaknesses requiring immediate attention
- Prioritization of remediation by business impact (vs. equal treatment of all gaps)
- Connection of technical control failures to business consequences

**Decision Support:**

- Evidence-based assessment enabling informed IPO timing decisions
- Resource allocation guidance for control remediation efforts
- Baseline for measuring remediation progress

### Skills Applied to Real-World Scenarios

This virtual internship simulated authentic consulting engagement deliverables including:

- Client documentation review and analysis
- Stakeholder interviews under time constraints
- Control testing with evidence documentation
- Executive reporting and presentation
- Remediation planning and project phasing

The project demonstrated core competencies required for:

- **SOC Analyst roles** - Understanding enterprise security controls, change management, access governance
- **GRC Analyst positions** - Risk assessment, compliance analysis, control testing, audit support
- **Security Consultant work** - Client engagement, gap analysis, stakeholder communication, remediation planning

-----

## Portfolio Note

This comprehensive analysis documents my independent work, analytical approach, and professional development from the PwC Cybersecurity & Controls job simulation on Forage. All scenario details, findings, and recommendations are presented in my own words to respect PwC’s intellectual property while demonstrating technical competencies and problem-solving capabilities.

This was a virtual simulation experience. No actual client data or proprietary PwC methodologies are included in this portfolio.

-----

**[← Back to Project Overview](./README.md)** | **[View on GitHub](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/Virtual-Internships/PwC-Cyber)**
