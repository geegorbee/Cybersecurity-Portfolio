# Task 1: Procure-to-Pay (P2P) Process Risk Assessment

**[← Back to Project Overview](../README.md)**

-----

## Objective

Analyze MedTech Industries’ Procure-to-Pay standard operating procedures to identify control gaps and assess SOX compliance readiness for their upcoming IPO.

-----

## Scenario Context

MedTech Industries, a healthcare startup, is preparing for an Initial Public Offering (IPO) next year. Once public, the company must comply with Sarbanes-Oxley (SOX) regulations. Initial assessments indicated their current P2P processes would likely not meet SOX requirements.

**My Role:** Review the client’s P2P Standard Operating Procedure (SOP), identify existing control gaps that may pose risks, and communicate findings to the senior associate.

-----

## Methodology

1. **Document Review:** Analyzed MedTech’s P2P SOP documentation
1. **Framework Comparison:** Compared current processes against:
- SOX Section 404 requirements
- COSO Internal Control Framework
- Industry best practices for financial controls
1. **Gap Analysis:** Identified missing or insufficient controls
1. **Risk Mapping:** Connected process gaps to specific business risks
1. **Recommendations:** Developed actionable remediation strategies

-----

## Key Findings

### Access Control & Identity Management Gaps

**Finding 1: Shared Credentials**

- **Gap:** Inventory team uses shared passwords for system access
- **Risk:** Loss of accountability and audit trail; inability to track who performed specific actions
- **Impact:** Non-compliance with SOX individual accountability requirements
- **Recommendation:** Implement unique user credentials with individual authentication

**Finding 2: Informal Access Provisioning**

- **Gap:** Anyone can request access to purchasing system; admin rights granted via phone call
- **Risk:** Unauthorized access to financial systems; excessive privileges granted without validation
- **Impact:** Fraud risk; failure of least-privilege principle
- **Recommendation:** Establish formal access request/approval workflow with role-based access controls (RBAC)

### Segregation of Duties (SoD) Violations

**Finding 3: Single-Person Transaction Control**

- **Gap:** One purchasing coordinator handles entire transaction lifecycle (requisition → approval → payment)
- **Risk:** Single point of failure; opportunity for unauthorized transactions or fraud
- **Impact:** Critical SOX compliance failure
- **Recommendation:** Separate responsibilities: different individuals for requisition, approval, and disbursement

**Finding 4: Self-Authorization of Payments**

- **Gap:** Purchasing coordinators can authorize and process payments for their own transactions
- **Risk:** Undetected errors or fraudulent payments
- **Impact:** Financial loss; audit findings
- **Recommendation:** Require independent authorization from finance/accounting team

**Finding 5: Inappropriate Invoice Verification**

- **Gap:** Invoices sent to warehouse/inventory team for verification instead of Finance/Accounting
- **Risk:** Business unit validating its own transactions (SoD violation)
- **Impact:** Potential for collusion or undetected errors
- **Recommendation:** Route invoices through Finance for three-way match validation

### Business Process Control Gaps

**Finding 6: Automated Approval Without Validation**

- **Gap:** Purchase requisitions automatically approved via system configuration
- **Risk:** Unauthorized or inappropriate purchases approved without oversight
- **Impact:** Budget overruns; procurement of unnecessary items
- **Recommendation:** Implement approval threshold logic with human review for significant purchases

**Finding 7: Missing Three-Way Match**

- **Gap:** No validation that Purchase Order, Goods Receipt, and Invoice align before payment
- **Risk:** Payment for undelivered goods; incorrect quantities/pricing
- **Impact:** Financial loss; supplier disputes
- **Recommendation:** Deploy three-way match control as mandatory gate before payment processing

**Finding 8: No Supplier Due Diligence**

- **Gap:** Lack of vendor validation or due diligence process documented
- **Risk:** Payments to fraudulent vendors; substandard suppliers
- **Impact:** Financial loss; operational disruptions
- **Recommendation:** Establish supplier onboarding process with validation checks

**Finding 9: Insufficient Cash Reconciliation**

- **Gap:** No evidence of regular cash reconciliation to bank statements
- **Risk:** Undetected errors or unauthorized transactions
- **Impact:** Financial statement inaccuracies; audit findings
- **Recommendation:** Implement monthly cash reconciliation performed by individual independent of payment processing

-----

## Risk Categorization

|**Risk Category**            |**Severity**|**SOX Impact**|**Gaps Contributing**|
|-----------------------------|------------|--------------|---------------------|
|Segregation of Duties Failure|Critical    |Yes           |Findings 3, 4, 5     |
|Access Control Weakness      |High        |Yes           |Findings 1, 2        |
|Financial Controls Missing   |Critical    |Yes           |Findings 6, 7, 9     |
|Vendor Management            |Medium      |Indirect      |Finding 8            |

-----

## Recommendations Summary

**Immediate Actions (0-30 days):**

1. Eliminate shared credentials; provision unique user accounts
1. Implement segregation of duties for payment authorization/processing
1. Deploy three-way match control for all payments

**Short-Term (30-90 days):**
4. Establish formal access request/approval workflow
5. Implement dual-signature requirements for disbursements above threshold
6. Begin monthly cash reconciliation process

**Medium-Term (90-180 days):**
7. Document and deploy vendor onboarding/validation procedures
8. Configure system controls to enforce approval workflows
9. Conduct quarterly access reviews to validate RBAC enforcement

-----

## Communication to Senior Associate

Delivered findings via email summarizing:

- **Cash Disbursement Control Risks:** 4 major risk categories identified
- **Business Process & IT Control Gaps:** 6 specific gaps documented with risk mapping
- **Follow-Up Questions:** 3 targeted questions to clarify undocumented controls

**Key Takeaway:** Emphasized that current P2P process had multiple critical SOX compliance gaps requiring remediation before IPO readiness.

-----

## Skills Demonstrated

✅ **Risk Assessment:** Systematic identification of control weaknesses  
✅ **SOX Compliance Knowledge:** Understanding of Section 404 requirements  
✅ **Segregation of Duties Analysis:** Identifying SoD violations in financial processes  
✅ **Access Control Evaluation:** RBAC and least-privilege principle application  
✅ **Business Process Analysis:** Mapping processes to control frameworks  
✅ **Professional Communication:** Translating technical findings into business risk language

-----

## Lessons Learned

**What Worked Well:**

- Comprehensive identification of multiple risk categories
- Clear connection between gaps and business impacts
- Practical, actionable recommendations

**Areas for Improvement:**

- Initial analysis could have been more structured by risk category (vs. listing gaps sequentially)
- Could have explicitly mapped each gap to specific SOX control objectives
- Follow-up questions could have been more targeted to validation vs. discovery

**Key Insight:** Effective risk communication requires organizing findings by impact level and connecting technical gaps to business consequences that non-technical stakeholders understand.

-----

## Related Tasks

- **[Task 2: SDLC Controls Walkthrough](../Task-2/)** - Applied similar gap analysis methodology to software development processes
- **[Task 3: Change Management Testing](../Task-3/)** - Tested operating effectiveness of access controls identified in Task 1
- **[Task 4: Executive Summary](../Task-4/)** - Synthesized P2P findings into leadership presentation

-----

**[← Back to Project Overview](../README.md)** | **[Next: Task 2 →](../Task-2/)**
