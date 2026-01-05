# Task 2: SDLC Controls Walkthrough

**[← Back to Project Overview](../README.md)**

-----

## Objective

Evaluate MedTech Industries’ Software Development Life Cycle (SDLC) process for their payroll system implementation against NIST standards and conduct an audit walkthrough with the IT manager to identify control gaps.

-----

## Scenario Context

MedTech is implementing a complete payroll system to replace their historical Excel-based process as part of IPO readiness. The IT manager (Bob) provided an SDLC Standard Operating Procedure based on NIST framework but with custom modifications.

**Challenge:** Bob had limited availability (30-minute meeting, declined multiple times previously) and was known for providing concise answers that might not fully explain processes.

**My Role:**

1. Analyze SDLC SOP against NIST SP 800-64 guidelines
1. Identify gaps between documented procedures and leading practices
1. Conduct structured walkthrough interview to clarify gaps
1. Obtain commitment for follow-up on unresolved questions

-----

## Methodology

### Phase 1: Pre-Walkthrough Analysis

**Framework Comparison:**

- Reviewed MedTech’s SDLC SOP (5 phases: Initiation, Development, Implementation, Operations & Maintenance, Decommission)
- Compared to NIST SP 800-64 Rev. 2 guidelines
- Identified potential gaps where client modifications deviated from best practices

**Walkthrough Preparation:**

- Developed risk-based question strategy prioritizing highest-impact gaps
- Created question sequence to maximize information gathering in limited time
- Prepared follow-up paths based on anticipated responses

### Phase 2: Structured Interview Execution

**Interview Strategy:**

- Started with open-ended walkthrough request (establish baseline understanding)
- Moved to targeted gap-clarification questions
- Used probing questions to understand actual vs. documented practices
- Documented commitment for post-meeting follow-up on remaining items

-----

## Key Findings

### Gap 1: Missing Design Reviews Before Production Deployment

**Documentation Review:**

- NIST framework recommends design reviews at phase transitions to validate requirements are met
- MedTech SOP did not explicitly mention design review activities

**Walkthrough Clarification:**

- **Question Asked:** “Are design reviews performed before placing the system into operation to ensure it meets all required specifications?”
- **Response:** “No, we take the requirements at face value when provided during planning and development. If that’s what they submitted, that’s what they wanted.”

**Analysis:**

- **Gap Confirmed:** No formal design review process exists
- **Risk:** Systems deployed to production may not meet business requirements or security specifications
- **Impact:** Costly post-implementation rework; potential regulatory non-compliance; user dissatisfaction
- **Recommendation:** Implement mandatory design review checkpoints before each phase transition with sign-off requirements

### Gap 2: Undocumented Configuration Management

**Documentation Review:**

- NIST framework emphasizes configuration management (CM) and control activities
- MedTech SOP did not include CM procedures in Operations & Maintenance section

**Walkthrough Clarification:**

- **Question Asked:** “I didn’t see mention of configuration management and control activities for proposed or actual changes to the system. Is this something you have in place?”
- **Response:** “Yes, we have configuration management activities but forgot to put them in the SOP. I’ll make sure we add it.”

**Analysis:**

- **Gap Type:** Documentation gap (process exists but undocumented)
- **Risk:** Audit findings; inconsistent application of CM procedures without formal documentation
- **Impact:** Difficulty training new staff; inability to demonstrate control existence during audits
- **Recommendation:** Formally document CM procedures and integrate into SDLC SOP with version control

### Gap 3: Insufficient Testing Documentation

**Documentation Review:**

- Testing activities mentioned but lacked detail on evidence requirements

**Walkthrough Clarification:**

- **Question Asked:** “Could you elaborate on the functional and security testing performed during development?”
- **Response:** Confirmed testing occurs but did not provide documentation standards

**Analysis:**

- **Gap:** Lack of audit trail for testing activities
- **Risk:** Inability to prove testing was completed; potential audit findings
- **Impact:** Difficulty demonstrating due diligence during compliance reviews
- **Recommendation:** Establish testing documentation standards with sign-off requirements and evidence retention

-----

## Walkthrough Interview Flow

**Opening (Relationship Building):**

- Acknowledged time constraint
- Confirmed understanding of documented SDLC process
- Requested focused clarification on specific areas

**Discovery Questions (Gap Clarification):**

|**Question Type**|**Purpose**              |**Example**                                                                     |
|-----------------|-------------------------|--------------------------------------------------------------------------------|
|Open-ended       |Baseline understanding   |“Could you walk us through MedTech’s SDLC process?”                             |
|Targeted gap     |Validate suspected issues|“Are design reviews performed before go-live?”                                  |
|Probing          |Understand depth         |“Could you elaborate on functional and security testing?”                       |
|Validation       |Confirm recommendations  |“Leading practices recommend design reviews - is this something you’d consider?”|

**Closing (Commitment to Follow-Up):**

- Acknowledged time limitation
- Secured commitment for email follow-up on remaining questions
- Requested brief follow-up meeting to review outstanding items

-----

## Audit Walkthrough Best Practices Applied

✅ **Preparation:** Thoroughly reviewed documentation before meeting  
✅ **Efficiency:** Prioritized highest-risk gaps given time constraint  
✅ **Flexibility:** Adjusted question strategy based on responses  
✅ **Documentation:** Took detailed notes on responses and commitments  
✅ **Follow-Up:** Secured path forward for unresolved questions  
✅ **Relationship:** Maintained collaborative tone despite finding gaps

-----

## Skills Demonstrated

✅ **Framework Knowledge:** Application of NIST SP 800-64 SDLC standards  
✅ **Gap Analysis:** Systematic comparison of documented vs. leading practices  
✅ **Interview Techniques:** Structured questioning to maximize limited time  
✅ **Active Listening:** Identifying undocumented processes through follow-up questions  
✅ **Risk Assessment:** Prioritizing gaps by potential business impact  
✅ **Professional Communication:** Delivering findings as recommendations vs. criticism  
✅ **Stakeholder Management:** Working with time-constrained, reluctant interviewees

-----

## Recommendations Summary

|**Gap**                        |**Severity**|**Recommendation**                                       |**Timeline**|
|-------------------------------|------------|---------------------------------------------------------|------------|
|No design reviews              |High        |Implement review gates with sign-off before deployment   |30-60 days  |
|Undocumented CM                |Medium      |Formalize and document CM procedures in SDLC SOP         |30 days     |
|Insufficient test documentation|Medium      |Establish testing evidence standards and retention policy|60-90 days  |

-----

## Lessons Learned

**Effective Walkthrough Strategies:**

- **Pre-work is critical:** Detailed document review enables targeted questions
- **Start broad, then narrow:** Open questions establish baseline before drilling into gaps
- **Read between the lines:** “We forgot to document it” suggests process may be informal or inconsistent
- **Maintain collaboration:** Framing gaps as improvement opportunities vs. failures preserves relationship

**Time Management with Constrained Stakeholders:**

- Prioritize highest-impact questions first
- Accept that not everything will be resolved in one meeting
- Secure commitment for follow-up before meeting ends
- Be prepared to pivot based on stakeholder responses

**Documentation Standards Matter:**

- Even when processes exist, lack of documentation creates audit risk
- Undocumented controls are difficult to consistently apply
- Formalization enables training, monitoring, and improvement

-----

## Connection to Other Tasks

- **[Task 1: P2P Analysis](../Task-1/)** - Similar framework comparison methodology applied to financial processes
- **[Task 3: Change Management Testing](../Task-3/)** - Follow-up on configuration management gaps identified here
- **[Task 4: Executive Summary](../Task-4/)** - SDLC gaps incorporated into overall risk assessment

-----

## Related NIST Resources

- **NIST SP 800-64 Rev. 2:** Security Considerations in the System Development Life Cycle
- **NIST SP 800-53:** Security and Privacy Controls for Information Systems
- **NIST Cybersecurity Framework:** Core functions applied to SDLC phases

-----

**[← Task 1](../Task-1/)** | **[Back to Overview](../README.md)** | **[Task 3 →](../Task-3/)**
