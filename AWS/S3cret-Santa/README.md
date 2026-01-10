# AWS Security Analysis - S3cret Santa

**Lab:** TryHackMe Advent of Cyber 2025 Day 23  
**Completed:** December 2025 | Documented: January 9, 2026  
**Focus:** AWS IAM privilege enumeration, role assumption, and S3 security analysis

## Executive Summary

Performed hands-on AWS security analysis simulating an attacker scenario where compromised credentials were used to enumerate IAM permissions, assume privileged roles, and access sensitive data in S3 buckets. This exercise demonstrates practical understanding of AWS security concepts, IAM policy analysis, and cloud access control principles—directly applicable to GRC automation and cloud infrastructure control validation.

## Scenario

**The Setup:** An infiltrated agent discovered cloud credentials belonging to "Sir Carrotbane" and suspected they could provide access to The Best Festival Company's (TBFC) cloud network. The mission: enumerate privileges, identify access paths, and determine what sensitive data could be accessed.

**The Challenge:** Starting with limited credentials, identify what permissions are available, discover privilege escalation paths, and ultimately access restricted resources—all while documenting the control gaps that enabled this access.

## Key Learning Objectives

✅ AWS account fundamentals and credential management  
✅ IAM privilege enumeration from an attacker's perspective  
✅ AWS CLI automation for security analysis  
✅ Role assumption and temporary credential handling  
✅ S3 bucket security analysis and data exfiltration  

## Technical Environment

- **AWS CLI** - Command-line interface for AWS service interaction
- **AWS STS (Security Token Service)** - Temporary credential management
- **AWS IAM** - Identity and access management
- **AWS S3** - Object storage service

---

## Attack Path Summary

