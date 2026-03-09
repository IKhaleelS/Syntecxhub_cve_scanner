import re


# Common port → service mapping
PORT_SERVICE_MAP = {
    21: "FTP",
    22: "OpenSSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "Apache",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
}


def detect_service(banner, port):

    banner_lower = banner.lower()

    # Banner-based detection first
    if "apache" in banner_lower:
        return "Apache"

    if "nginx" in banner_lower:
        return "Nginx"

    if "openssh" in banner_lower:
        return "OpenSSH"

    if "postfix" in banner_lower:
        return "Postfix"

    if "smtp" in banner_lower:
        return "SMTP"

    if "mysql" in banner_lower:
        return "MySQL"

    # Fallback: detect from port
    return PORT_SERVICE_MAP.get(port, "Unknown")


def extract_version(banner):

    version_pattern = r"\d+\.\d+(\.\d+)?"

    match = re.search(version_pattern, banner)

    if match:
        return match.group()

    return "Unknown"
