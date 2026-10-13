# Network Traffic & Packet Analysis

## Project Overview
Conducted a hands-on network traffic analysis using TShark in a cloud-based Linux environment. Captured and examined TCP and HTTP packets to understand network communication, connection establishment, and protocol behavior.

## Tools Used
- TShark (Wireshark CLI)
- GitHub Codespaces
- Linux
- Python HTTP Server
- cURL

## Security Objectives
- Capture live network traffic
- Identify source and destination IP addresses
- Examine TCP connection establishment
- Analyze HTTP requests and responses
- Document network security findings

## Lab Environment
Environment: GitHub Codespaces (Linux)
Network Interface: Loopback (lo)
Test Server: Python HTTP Server
Server Port: 8765
IP Address: 127.0.0.1

All traffic was generated within an authorized test environment.

## Network Investigation

### Finding 1: TCP Connection Establishment
Captured TCP synchronization packets associated with a connection to port 8765.

Observed:
- TCP SYN packet
- TCP SYN-ACK response
- Communication over the loopback interface

These packets demonstrate the initial stages of TCP connection establishment.

### Finding 2: HTTP Traffic Analysis
Captured and inspected an HTTP request and response.

Observed:
- HTTP HEAD / HTTP/1.1 request
- HTTP/1.0 200 OK response
- Source IP: 127.0.0.1
- Destination IP: 127.0.0.1

The HTTP 200 response confirmed successful communication with the local test server.

## Security Assessment
The observed packets were consistent with expected local web server activity.

No malicious activity was identified in the traffic examined. This exercise focused on network protocol analysis rather than attack detection.

## Security Recommendations
- Monitor unusual network connections
- Investigate unexpected ports and destinations
- Review suspicious TCP connection patterns
- Use encrypted protocols for sensitive communications
- Maintain network monitoring and logging

## Project Evidence
- http_capture.pcapng: Captured network packets
- http_findings.txt: HTTP traffic analysis
- tcp_handshake_findings.txt: TCP synchronization packet analysis

## Conclusion
Successfully captured and analyzed live TCP and HTTP network traffic using TShark. Demonstrated foundational skills in packet inspection, traffic filtering, TCP/IP analysis, and documenting network observations.

## Disclaimer
All analysis was conducted in an authorized cloud-based laboratory environment.