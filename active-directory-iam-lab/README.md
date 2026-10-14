
# Active Directory & Identity Access Management Lab

## Project Overview
Built a Samba Active Directory-compatible domain controller in a cloud-based Linux environment to practice identity provisioning, security group administration, and access auditing.

## Tools Used
- Samba Active Directory
- Docker
- GitHub Codespaces
- Linux
- Samba CLI

## Lab Configuration
Domain: DOMAIN1
Environment: Fedora Linux container

## IAM Tasks Completed
- Configured an Active Directory-compatible domain
- Created Help Desk and Finance security groups
- Provisioned test employee accounts
- Assigned users to department-specific groups
- Verified security group membership
- Reviewed Domain Admins membership
- Successfully authenticated a Finance test account
- Generated group membership audit evidence

## Security Groups
GG_Helpdesk_Tier1
- helpdesk.trainee

GG_Finance_Restricted
- finance.analyst

## Access Control Assessment
Configured a restricted Finance file share using Samba.

Successfully verified Finance account authentication against the standard SYSVOL share.

Separate interactive access tests demonstrated that finance.analyst could access the Finance-Restricted share while helpdesk.trainee received NT_STATUS_ACCESS_DENIED.

These observations are documented in iam_access_verification.md. Attempts to record the interactive tests produced connection errors and are not presented as successful recordings.

## Security Principles
- Identity and Access Management
- Role-Based Access Control
- Least Privilege
- Separation of Duties
- Access Auditing

## Evidence
iam_evidence.txt

## Further Validation
- Capture reproducible access test output without exposing passwords.
- Investigate connection errors during recorded test sessions.
- Review share and filesystem permissions for least privilege.

## Disclaimer
All accounts, groups, and resources were created in an authorized training environment.
