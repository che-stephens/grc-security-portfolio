# Python Security Log Automation

## Project Overview
Developed a Python security log analyzer to identify suspicious authentication activity and potential brute-force login attempts.

## Tools Used
- Python 3
- GitHub Codespaces
- Linux Terminal
- Visual Studio Code

## Security Objectives
- Analyze SSH authentication logs
- Identify failed login attempts
- Extract source IP addresses
- Detect repeated authentication failures
- Generate security findings

## Lab Results
Analyzed simulated authentication logs containing:

- 6 failed login attempts
- 2 source IP addresses
- 1 potential brute-force alert
- Alert threshold: 3 failed attempts

## Key Findings
IP address 192.0.2.10 generated four failed login attempts, exceeding the configured detection threshold.

## Security Recommendations
- Implement account lockout or login rate limiting
- Monitor repeated authentication failures
- Use multi-factor authentication
- Investigate suspicious login patterns

## How to Run
python3 log_analyzer.py

## Project Files
- log_analyzer.py: Python security analysis script
- sample_auth.log: Simulated authentication logs
- security_findings.txt: Generated security report

## Disclaimer
This project uses simulated security events in an authorized training environment.