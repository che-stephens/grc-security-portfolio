# IAM Access Control Verification

## Authorized Finance Access
Account: DOMAIN1\finance.analyst
Resource: Finance-Restricted
Observed result: Successful directory listing
Status: PASS

## Unauthorized Help Desk Access
Account: DOMAIN1\helpdesk.trainee
Resource: Finance-Restricted
Observed result: NT_STATUS_ACCESS_DENIED
Status: PASS

## Evidence Notes
Results were observed during separate access tests and documented using screenshots.

Attempts to capture interactive sessions produced connection errors. Those recordings are not considered proof of successful access control enforcement.

## Conclusion
The independent tests demonstrated authorized Finance access and denied Help Desk access to the restricted Samba share.
