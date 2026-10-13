
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

Finance share access testing remains unresolved due to a connection error. Authorization enforcement has not yet been verified.

## Security Principles
- Identity and Access Management
- Role-Based Access Control
- Least Privilege
- Separation of Duties
- Access Auditing

## Evidence
iam_evidence.txt

## Future Improvements
- Troubleshoot Finance share connectivity
- Verify authorized Finance access
- Verify unauthorized Help Desk access is denied
- Document successful positive and negative access tests

## Disclaimer
All accounts, groups, and resources were created in an authorized training environment.
