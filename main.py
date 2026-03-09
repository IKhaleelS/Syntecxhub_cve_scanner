import argparse

from scanner.port_scanner import scan_ports
from scanner.banner_grabber import grab_banner
from scanner.service_detector import detect_service, extract_version

from vulnerability.cve_lookup import check_vulnerabilities
from reports.report_generator import generate_report
from colorama import Fore, Style, init

init(autoreset=True)


def parse_args():

    parser = argparse.ArgumentParser(description="SyntexHub Vulnerability Scanner")

    parser.add_argument("--target", required=True, help="Target IP address")
    parser.add_argument("--start-port", type=int, default=1, help="Start port")
    parser.add_argument("--end-port", type=int, default=1024, help="End port")
    parser.add_argument("--threads", type=int, default=100, help="Number of scanning threads")
    parser.add_argument("--severity", help="Filter vulnerability severity")

    return parser.parse_args()

def color_severity(severity):

    if severity == "CRITICAL":
        return Fore.RED + severity + Style.RESET_ALL

    if severity == "HIGH":
        return Fore.LIGHTRED_EX + severity + Style.RESET_ALL

    if severity == "MEDIUM":
        return Fore.YELLOW + severity + Style.RESET_ALL

    if severity == "LOW":
        return Fore.GREEN + severity + Style.RESET_ALL

    return severity

def main():

    args = parse_args()

    print("\n===================================================")
    print("SyntecxHub Vulnerability Scanner - Grimmox Edition")
    print("======================================================")

    print(f"Target: {args.target}")
    print(f"Port Range: {args.start_port}-{args.end_port}")
    print(f"Threads: {args.threads}")

    print("\nScanning ports...\n")

    open_ports = scan_ports(
        args.target,
        args.start_port,
        args.end_port,
        args.threads
    )

    scan_results = []

    if not open_ports:
        print("No open ports found.")
        return

    for port in open_ports:

        banner = grab_banner(args.target, port)

        service = detect_service(banner, port)

        version = extract_version(banner)

        print(f"\n[OPEN] Port {port}")
        print(f"Service: {service}")
        print(f"Version: {version}")

        vulnerabilities = check_vulnerabilities(service, version)

        if vulnerabilities:

            print("\nPossible Vulnerabilities:\n")

            for vuln in vulnerabilities:

                if args.severity and vuln["severity"] != args.severity:
                   continue
                sev = color_severity(vuln['severity'])
                print(f"[{sev}] {vuln['cve']}")
                print(vuln['description'])
                print("-" * 40)

                scan_results.append({
                    "port": port,
                    "service": service,
                    "version": version,
                    "cve": vuln['cve'],
                    "severity": vuln['severity'],
                    "description": vuln['description']
                })

    generate_report(args.target, scan_results)


if __name__ == "__main__":
    main()
