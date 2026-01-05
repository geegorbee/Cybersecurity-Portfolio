# Task 3: Change Management Control Testing

**[← Back to Project Overview](../README.md)**

-----

## Objective

Document Test of Design (ToD) and Test of Operating Effectiveness (ToE) for change management controls over the CorpLaw application, validating that controls are properly designed and functioning as intended.

-----

## Scenario Context

Following successful walkthroughs of P2P and SDLC processes, I led the walkthrough meeting for CorpLaw system change management controls with IT Manager John Wilkins. The engagement partner provided notes and evidence to document formal control testing results.

**My Role:**

1. Review walkthrough notes and supporting evidence
1. Document Test of Design for two change management controls
1. Execute Test of Operating Effectiveness by examining samples
1. Identify and document control exceptions with supporting evidence

-----

## Control Testing Methodology

### Test of Design (ToD)

**Purpose:** Validate that controls are designed appropriately to address identified risks

**Approach:**

- Review control description and intended operation
- Compare to industry best practices (ITIL, COBIT)
- Assess whether control design adequately mitigates target risk
- Document design exceptions if control logic has flaws

### Test of Operating Effectiveness (ToE)

**Purpose:** Validate that controls are operating as designed in practice

**Approach:**

- Select representative sample of transactions/events
- Inspect evidence that control was executed
- Compare actual execution to expected design
- Document operating exceptions when control fails or is bypassed

-----

## Control 1.2: Emergency Change Authorization

### Control Design Documentation

**Control Objective:** Ensure emergency changes are properly authorized and reviewed even when expedited approval is necessary.

**Control Description:**
Emergency changes to the CorpLaw application follow a modified approval process:

1. Change request must be authorized by appropriate business owner
1. IT Director (Scott Trist) must approve within 24 hours of implementation
1. Change Advisory Board (CAB) must provide retrospective approval within 5 days of implementation

**Rationale:** Emergency changes require rapid deployment but still need oversight to prevent unauthorized modifications and ensure proper testing.

**Test of Design Result:** ✅ **No design exceptions noted.** Control is appropriately designed to balance speed with accountability.

-----

### Test of Operating Effectiveness

**Sample Selected:** Change Request (CR) Ticket #150  
**Change Type:** Emergency change to CorpLaw system  
**Implementation Date:** February 7, 2022

**Expected Evidence:**

1. Business authorization from appropriate owner
1. IT Director approval within 24 hours (by Feb 8, 2022)
1. CAB approval within 5 days (by Feb 12, 2022)
1. Evidence of testing in development and QA environments
1. User Acceptance Testing (UAT) approval from requestor

**Actual Evidence Observed:**

|**Control Step**      |**Expected**                 |**Actual**      |**Status**|
|----------------------|-----------------------------|----------------|----------|
|Business Authorization|Harvey Jones (Head of Law)   |Harvey Jones ✓  |Pass      |
|Development Approval  |Melissa Smith (Dev Team Lead)|Melissa Smith ✓ |Pass      |
|Testing (DEV/QA)      |Separate environments        |Completed ✓     |Pass      |
|UAT Approval          |Harvey Jones                 |Harvey Jones ✓  |Pass      |
|IT Director Approval  |Scott Trist within 24 hrs    |**Harvey Jones**|**FAIL**  |
|CAB Approval          |Within 5 days                |**No evidence** |**FAIL**  |

### Control Exception Identified

**Exception:** Control 1.2 failed Test of Operating Effectiveness

**Specific Failures:**

1. **Wrong Approver:** CR150 was approved by Harvey Jones (requestor/business owner) instead of Scott Trist (IT Director)
1. **Missing CAB Approval:** No evidence of Change Advisory Board approval within required 5-day window

**Risk Impact:**

- Emergency changes deployed without IT oversight
- Potential for business units to bypass technical validation
- No secondary review to catch technical or security issues
- Pattern suggests control may be routinely circumvented

**Root Cause Analysis:**

- Possible lack of awareness of emergency change procedures
- Potential system configuration allowing wrong approver
- May indicate insufficient training or enforcement

**Recommendation:**

- **Immediate:** Implement weekly automated review of all emergency changes to validate proper approval chain
- **Short-term:** Configure system to enforce specific approvers based on change type
- **Long-term:** Conduct training on emergency vs. standard change procedures; add automated alerts when approval requirements not met

-----

## Control 1.3: Segregation of Duties (Developer/Implementer Roles)

### Control Design Documentation

**Control Objective:** Prevent single individuals from developing and deploying code changes, ensuring independent review and reducing fraud/error risk.

**Control Description:**
Two distinct system roles enforce segregation of duties in CorpLaw change management:

1. **“CorpLawDev” role** - Granted to developers for code creation and testing
1. **“CorpLawImp” role** - Granted to implementers for production deployment

**Design Requirement:** No user should have both roles simultaneously. Users in each group must be unique to maintain separation.

**Test of Design Result:** ✅ **No design exceptions noted.** Control design appropriately enforces segregation of duties through role-based access control (RBAC).

-----

### Test of Operating Effectiveness

**Sample Selected:** Complete population of users in both CorpLawDev and CorpLawImp role groups  
**Test Date:** June 24, 2022 (walkthrough date)

**Testing Procedure:**

1. Exported list of all users with CorpLawDev role
1. Exported list of all users with CorpLawImp role
1. Performed comparison to identify any users appearing in both lists
1. Validated that identified users were active (not disabled accounts)

**Expected Result:** Zero users with access to both roles

**Actual Result:** One user identified in both role groups

### Control Exception Identified

**Exception:** Control 1.3 failed Test of Operating Effectiveness

**Specific Finding:**

- **User:** Martin France
- **Access:** Active membership in both CorpLawDev and CorpLawImp groups
- **Status:** Both roles were active at time of testing

**Segregation of Duties Conflict:**
Martin France has ability to:

- Develop code changes (CorpLawDev role)
- Deploy those same changes to production (CorpLawImp role)
- Effectively bypass independent review and approval

**Risk Impact:**

- Single user can introduce unauthorized code into production
- No independent validation of code changes
- Potential for undetected errors or malicious changes
- Violation of separation of duties principle required by SOX
- Increased fraud risk

**Root Cause Analysis:**

- Likely result of job role transition without proper access cleanup
- Possible temporary access granted that was never revoked
- May indicate lack of regular access certification reviews

**Recommendation:**

- **Immediate:** Revoke Martin France’s access to one of the conflicting roles based on current job responsibilities
- **Short-term:** Implement quarterly access certification reviews where managers validate role assignments
- **Long-term:** Deploy automated system alerts when users are added to conflicting role groups; integrate access reviews into job transition workflow (joiner/mover/leaver process)

-----

## Control Testing Summary

|**Control**                         |**Test of Design**|**Test of Operating Effectiveness**|**Exceptions**                                 |
|------------------------------------|------------------|-----------------------------------|-----------------------------------------------|
|1.2 - Emergency Change Authorization|✅ Pass            |❌ Fail                             |Wrong approver; missing CAB approval           |
|1.3 - Developer/Implementer SoD     |✅ Pass            |❌ Fail                             |User with both developer and implementer access|

-----

## Impact Assessment

**Severity:** Both exceptions are **HIGH SEVERITY**

**Compliance Impact:**

- SOX Section 404 requires effective internal controls over financial systems
- CorpLaw likely supports legal/compliance functions affecting financial reporting
- Control failures create audit findings and potential material weakness designation

**Business Impact:**

- Increased risk of unauthorized system changes
- Potential for fraud or errors to go undetected
- Reputation risk if control weaknesses discovered during IPO due diligence

**Remediation Priority:** Both exceptions require immediate attention before IPO process advances.

-----

## Skills Demonstrated

✅ **Control Testing Expertise:** Understanding of Test of Design vs. Test of Operating Effectiveness  
✅ **Audit Documentation:** Professional format following industry standards  
✅ **Evidence Analysis:** Comparing expected vs. actual control execution  
✅ **Exception Identification:** Recognizing control failures with supporting evidence  
✅ **Risk Assessment:** Evaluating business impact of control exceptions  
✅ **Root Cause Analysis:** Identifying why controls failed  
✅ **Remediation Planning:** Developing practical, risk-based recommendations  
✅ **RBAC & IAM Knowledge:** Understanding segregation of duties in access control  
✅ **Change Management:** ITIL change control principles

-----

## Lessons Learned

**Control Testing Discipline:**

- Compare actual evidence to expected behavior systematically
- Don’t assume controls work because they’re documented
- Explicitly state pass/fail status for each control element
- Document exceptions with specific evidence, not just general observations

**Importance of Access Reviews:**

- Both exceptions could have been detected through regular reviews
- Automated monitoring can catch violations in real-time
- Access governance is continuous process, not one-time setup

**Professional Documentation Standards:**

- Clear structure makes findings easy to understand and action
- Separating design from operating effectiveness clarifies issue type
- Specific recommendations with timelines enable accountability

**Communication of Negative Findings:**

- Frame exceptions as opportunities for improvement
- Provide context on why control is important (link to risk)
- Offer practical remediation, not just criticism
- Distinguish between design flaws vs. execution failures

-----

## Connection to Other Tasks

- **[Task 1: P2P Analysis](../Task-1/)** - Similar segregation of duties issues identified in financial processes
- **[Task 2: SDLC Walkthrough](../Task-2/)** - Configuration management gaps (identified here) were undocumented there
- **[Task 4: Executive Summary](../Task-4/)** - Both exceptions elevated as critical findings requiring leadership attention

-----

## Related Frameworks & Standards

- **ITIL Change Management:** Best practices for change control and emergency changes
- **COBIT 5:** BAI06 - Manage Changes; DSS05 - Manage Security Services
- **SOX Section 404:** Internal control requirements for financial systems
- **NIST SP 800-53:** AC-5 (Separation of Duties), CM-3 (Configuration Change Control)

-----

**[← Task 2](../Task-2/)** | **[Back to Overview](../README.md)** | **[Task 4 →](../Task-4/)**
