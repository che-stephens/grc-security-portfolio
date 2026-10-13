
from collections import Counter
from pathlib import Path

# Security log configuration
LOG_FILE = Path("sample_auth.log")
ALERT_THRESHOLD = 3

def analyze_logs():
    if not LOG_FILE.exists():
        print("Log file not found.")
        return

    failed_logins = []

    with LOG_FILE.open("r") as file:
        for line in file:
            if "Failed password" in line and "from " in line:
                ip_address = line.split("from ")[1].split()[0]
                failed_logins.append(ip_address)

    login_counts = Counter(failed_logins)

    print("SECURITY LOG ANALYSIS REPORT")
    print("----------------------------")
    print(f"Total failed logins: {len(failed_logins)}")

    for ip, count in login_counts.items():
        print(f"\nIP Address: {ip}")
        print(f"Failed attempts: {count}")

        if count >= ALERT_THRESHOLD:
            print("ALERT: Possible brute-force activity")
        else:
            print("Status: Below alert threshold")

if __name__ == "__main__":
    analyze_logs()
