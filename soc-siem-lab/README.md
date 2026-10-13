SOC Security Monitoring & Threat Detection Lab

Project Overview

Built a cloud-based security monitoring lab using Wazuh Manager to analyze simulated authentication events, test security detection rules, and document incident investigation findings.

Technologies Used

Wazuh Manager 4.14.8
Wazuh Logtest
Docker
Linux
GitHub Codespaces

Project Objectives

Configure a security detection environment
Verify Wazuh monitoring services
Analyze simulated SSH authentication events
Identify matching security detection rules
Interpret security alert severity levels
Document incident investigation findings

Lab Configuration

Deployed Wazuh Manager inside a Docker container hosted in GitHub Codespaces.

Verified that the Wazuh analysis engine and log collector were operational.

Used Wazuh Logtest to submit simulated security events and evaluate detection rules.

Security Detection Results

Event: Failed SSH login attempt

Source IP Address: 192.0.2.10

Attempted Username: trainee

Detection Rule: 5710

Alert Level: 5

Result: Wazuh successfully identified an authentication attempt involving a nonexistent user.

Incident Investigation

Analyzed the generated alert to identify the authentication event, source IP address, attempted username, and associated detection rule.

Documented the findings and recommended response actions in a separate incident investigation report.

The test involved simulated activity, not an actual compromise.

Security Recommendations

Monitor repeated authentication failures
Investigate suspicious IP addresses
Review account access and authentication policies
Implement appropriate account protection measures
Correlate authentication events with additional security logs
Escalate confirmed threats according to incident response procedures

Project Documentation

incident_report.md — Security incident investigation report
wazuh_detection_evidence.txt — Detection evidence file pending verification

Skills Demonstrated

Security log analysis
SOC alert triage
Rule-based threat detection
SSH authentication monitoring
Security incident documentation
Incident response recommendations

Lab Limitations

This project used Wazuh Manager’s detection-testing capabilities rather than a complete production SIEM deployment.

Security events were simulated and submitted manually. The Wazuh container was removed after testing to recover cloud storage.

Conclusion

Successfully tested Wazuh’s detection engine, analyzed a simulated SSH authentication failure, identified a matching security rule, and documented investigation findings.

Disclaimer

All testing was conducted within an authorized cloud-based cybersecurity laboratory using simulated security events.