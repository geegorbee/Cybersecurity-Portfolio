"""
GRC Evidence Collection Automation
Author: Gerald Brown
Date: January 2026

Demonstrates programmatic evidence gathering for SOC 2 compliance frameworks.
Simulates automated collection, tagging, and reporting of audit evidence.

Real-world application: Reduce manual evidence collection time by ~60%,
enable continuous compliance monitoring, support multiple audit frameworks.
"""

import json
import csv
from datetime import datetime, timedelta
import os

# ============================================================================
# EVIDENCE TAGGING SYSTEM
# ============================================================================

def tag_evidence(control_id, framework, evidence_type, source, description, status="collected"):
    """
    Create standardized evidence metadata tag.
    
    Args:
        control_id: Framework control identifier (e.g., "CC6.1")
        framework: Compliance framework (e.g., "SOC2_Type2")
        evidence_type: Type of evidence (e.g., "access_logs", "siem_alerts")
        source: Source system (e.g., "AWS_IAM", "Splunk")
        description: Human-readable description
        status: Evidence status (collected, reviewed, validated)
    
    Returns:
        Dictionary with standardized evidence metadata
    """
    return {
        "evidence_id": f"{control_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "control_id": control_id,
        "framework": framework,
        "evidence_type": evidence_type,
        "source_system": source,
        "description": description,
        "status": status,
        "collection_date": datetime.now().strftime("%Y-%m-%d"),
        "reviewer": None,
        "notes": None
    }

# ============================================================================
# EVIDENCE COLLECTION FUNCTIONS (SOC 2 CONTROLS)
# ============================================================================

def collect_access_control_evidence():
    """
    CC6.1: Logical and Physical Access Controls
    
    Simulates collecting IAM policy and RBAC evidence.
    Real implementation would query AWS IAM, Azure AD, or similar.
    """
    evidence_items = []
    
    # User access review evidence
    evidence_items.append(tag_evidence(
        control_id="CC6.1",
        framework="SOC2_Type2",
        evidence_type="access_review",
        source="AWS_IAM",
        description="Quarterly user access review completed - 127 active users validated, 3 removed"
    ))
    
    # RBAC configuration evidence
    evidence_items.append(tag_evidence(
        control_id="CC6.1",
        framework="SOC2_Type2",
        evidence_type="rbac_config",
        source="IAM_System",
        description="Role-based access control verified - least privilege principles enforced"
    ))
    
    # AWS Connect access management (from CRA experience)
    evidence_items.append(tag_evidence(
        control_id="CC6.1",
        framework="SOC2_Type2",
        evidence_type="cloud_access",
        source="AWS_Connect",
        description="Agent access permissions validated for telephony system - 24 active users"
    ))
    
    return evidence_items

def collect_monitoring_evidence():
    """
    CC7.2: System Monitoring
    
    Simulates collecting SIEM alerts and monitoring data.
    Real implementation would query Splunk, Sentinel, or similar.
    """
    evidence_items = []
    
    # SIEM monitoring evidence
    evidence_items.append(tag_evidence(
        control_id="CC7.2",
        framework="SOC2_Type2",
        evidence_type="siem_config",
        source="Splunk",
        description="Security monitoring rules active - 47 detection rules configured for anomaly detection"
    ))
    
    # Alert response evidence
    evidence_items.append(tag_evidence(
        control_id="CC7.2",
        framework="SOC2_Type2",
        evidence_type="alert_metrics",
        source="Splunk",
        description="Monthly alert summary - 234 alerts triggered, 12 investigated, 0 confirmed incidents"
    ))
    
    # CloudWatch monitoring (from AWS experience)
    evidence_items.append(tag_evidence(
        control_id="CC7.2",
        framework="SOC2_Type2",
        evidence_type="cloud_monitoring",
        source="AWS_CloudWatch",
        description="AWS Connect call quality monitoring active - connectivity metrics tracked"
    ))
    
    return evidence_items

def collect_incident_response_evidence():
    """
    CC7.4: Incident Response
    
    Simulates collecting IR documentation and response metrics.
    Real implementation would query ticketing systems, runbooks.
    """
    evidence_items = []
    
    # IR playbook evidence
    evidence_items.append(tag_evidence(
        control_id="CC7.4",
        framework="SOC2_Type2",
        evidence_type="ir_procedures",
        source="IR_Documentation",
        description="Incident response playbook reviewed and updated - 8 runbooks validated"
    ))
    
    # Incident metrics evidence
    evidence_items.append(tag_evidence(
        control_id="CC7.4",
        framework="SOC2_Type2",
        evidence_type="incident_metrics",
        source="Ticketing_System",
        description="Quarterly incident summary - 3 incidents detected, avg response time 45 minutes"
    ))
    
    return evidence_items

def collect_change_management_evidence():
    """
    CC8.1: Change Management
    
    Simulates collecting change control documentation.
    Real implementation would query change management systems.
    """
    evidence_items = []
    
    # Change approval evidence
    evidence_items.append(tag_evidence(
        control_id="CC8.1",
        framework="SOC2_Type2",
        evidence_type="change_approvals",
        source="Change_Management",
        description="Quarterly change review - 23 changes approved, all with testing validation"
    ))
    
    return evidence_items

def collect_risk_assessment_evidence():
    """
    CC9.1: Risk Assessment
    
    Simulates collecting risk assessment documentation.
    Real implementation would reference risk registers, assessments.
    """
    evidence_items = []
    
    # Annual risk assessment
    evidence_items.append(tag_evidence(
        control_id="CC9.1",
        framework="SOC2_Type2",
        evidence_type="risk_assessment",
        source="Risk_Register",
        description="Annual risk assessment completed - 15 risks identified, 12 mitigated, 3 accepted"
    ))
    
    return evidence_items

# ============================================================================
# EVIDENCE REPOSITORY MANAGEMENT
# ============================================================================

def save_evidence_json(evidence_list, output_file="evidence_collection.json"):
    """Save evidence to JSON file for programmatic access"""
    with open(output_file, 'w') as f:
        json.dump(evidence_list, f, indent=2)
    print(f"✓ Saved {len(evidence_list)} evidence items to {output_file}")

def generate_evidence_report(evidence_list, output_file="evidence_report.csv"):
    """Generate CSV report for audit review"""
    if not evidence_list:
        print("⚠ No evidence to report")
        return
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=evidence_list[0].keys())
        writer.writeheader()
        writer.writerows(evidence_list)
    print(f"✓ Generated {output_file} for audit review")

def generate_control_summary(evidence_list):
    """Generate summary of controls with evidence"""
    control_counts = {}
    for item in evidence_list:
        control = item['control_id']
        control_counts[control] = control_counts.get(control, 0) + 1
    
    print("\n" + "=" * 60)
    print("CONTROL COVERAGE SUMMARY")
    print("=" * 60)
    for control, count in sorted(control_counts.items()):
        print(f"  {control}: {count} evidence items")
    print("=" * 60)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main evidence collection workflow.
    
    In production, this would:
    - Connect to actual systems (AWS, Splunk, ticketing)
    - Pull real logs and metrics
    - Tag with control metadata
    - Generate audit packages
    """
    print("\n" + "=" * 60)
    print("GRC EVIDENCE COLLECTION AUTOMATION")
    print("SOC 2 Type II Compliance Framework")
    print("=" * 60)
    print(f"Collection Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Collect evidence from all control areas
    all_evidence = []
    
    print("\nCollecting evidence for SOC 2 controls...")
    print("-" * 60)
    
    print("  → CC6: Access Controls")
    all_evidence.extend(collect_access_control_evidence())
    
    print("  → CC7: System Monitoring & Incident Response")
    all_evidence.extend(collect_monitoring_evidence())
    all_evidence.extend(collect_incident_response_evidence())
    
    print("  → CC8: Change Management")
    all_evidence.extend(collect_change_management_evidence())
    
    print("  → CC9: Risk Assessment")
    all_evidence.extend(collect_risk_assessment_evidence())
    
    print(f"\n✓ Collected {len(all_evidence)} total evidence items")
    
    # Save evidence
    print("\nSaving evidence repository...")
    print("-" * 60)
    save_evidence_json(all_evidence)
    generate_evidence_report(all_evidence)
    
    # Generate summary
    generate_control_summary(all_evidence)
    
    print("\n" + "=" * 60)
    print("EVIDENCE COLLECTION COMPLETE")
    print("=" * 60)
    print("\nAudit-ready outputs:")
    print("  • evidence_collection.json (programmatic access)")
    print("  • evidence_report.csv (spreadsheet review)")
    print("\nNext steps:")
    print("  • Review evidence for completeness")
    print("  • Attach supporting documentation")
    print("  • Submit to auditor")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

