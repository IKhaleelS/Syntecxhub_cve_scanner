# SyntecxHub Vulnerability Scanner

A lightweight Python-based vulnerability scanner that performs **port scanning, service detection, and vulnerability identification using CVE data from the NVD API**.

This project was developed as part of a cybersecurity internship assignment.

---

## Features

- Multi-threaded TCP port scanning
- Banner grabbing for service detection
- Service version identification
- CVE vulnerability lookup using the NVD API
- Severity classification (CRITICAL, HIGH, MEDIUM, LOW)
- Colored vulnerability output
- JSON vulnerability reporting
- Command-line interface

---

## Technologies Used

- Python 3
- Requests library
- Colorama for terminal output
- NVD API (National Vulnerability Database)

---

## Project Structure


syntexhub-scanner/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
|__ vulnerability
|
└── reports/
└── scan_report.json


---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/syntexhub-scanner.git
cd syntexhub-scanner
```
Install dependencies:

``` pip install -r requirements.txt ```

 ## NVD API Setup

This scanner uses the NVD API to fetch vulnerability data.

Request a free API key from:

https://nvd.nist.gov/developers/request-an-api-key

Once obtained, add your key in the code where the API request is made.

## Usage

Basic scan:
``` python main.py --target scanme.nmap.org ```

Scan with severity filtering:

``` python main.py --target scanme.nmap.org --severity HIGH ``` 
Example Output
```
PORT SERVICE VERSION
--------------------------------
22 OpenSSH 8.2
80 Apache 2.4.49

\[HIGH] CVE-2021-41773
Apache HTTP Server Path Traversal Vulnerability
```
## Generated Reports

After each scan, a JSON report is saved:

``` reports/scan\_report.json ```


The report includes:

- scanned target
- open ports
- detected services
- discovered CVEs
- vulnerability descriptions
- severity ratings

## Limitations

- Banner grabbing may not always detect accurate service versions
- Vulnerability matching is based on detected service information
- Some CVEs may not contain severity data
- Future Improvements
- HTML vulnerability reports
- OS fingerprinting
- Network range scanning
- Service fingerprint database
- Web interface dashboard

## Legal Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Do not scan systems without proper permission.

## Author

Developed by Ibrahim Shafiu (SyntecxHub) as part of a cybersecurity internship project."# Syntecxhub_cve_scanner" 
