Port Scanner (simple-python-scanner)

A minimal, educational TCP port scanner written in Python using the standard socket library.
Scans a range of ports on a target IP and prints which ports are open. Intended only for learning and authorized testing.


---

Features

Single-file, dependency-free (uses Python standard library).

Scans a range of TCP ports.

Simple timeout control for connection attempts.

Beginner-friendly and easy to extend.



---

Requirements

Python 3.6+ (works with any modern Python 3.x)

No external packages required



---

Installation

1. Clone this repository or download the scanner.py file.


2. Make sure you have Python 3 installed:



python3 --version


---

Usage

Save the script as scanner.py (or whatever you prefer). Run it from a terminal:

python3 scanner.py

The script will prompt for:

Enter target IP address: — the IP address or hostname to scan (e.g., 192.168.1.10 or example.com)

Enter start port: — the first port in the range (e.g., 1)

Enter end port: — the last port in the range (e.g., 1024)


Example session:

$ python3 scanner.py
Enter target IP address: 192.168.1.10
Enter start port: 20
Enter end port: 25
Scanning target: 192.168.1.10 from port 20 to 25
Port 22 is open


---

Example script (for README reference)

import socket

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for connection attempts
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

target_ip = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"Scanning target: {target_ip} from port {start_port} to {end_port}")
for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)


---

Notes & Improvements

Timeout: The script uses a 1-second timeout. Increase or decrease s.settimeout(...) if you want faster scans or more tolerance for slow networks.

Performance: This scanner is sequential and can be slow for large ranges. Consider using threading or asyncio to parallelize scans for speed.

Port types: This only checks TCP ports (via socket.SOCK_STREAM). UDP scanning requires a different approach.

Permissions: Some ports/operations may require elevated privileges on certain systems.



---

Legal & Ethical Notice (READ THIS)

Only scan systems you own or have explicit permission to test. Unauthorized scanning of networks or systems may be illegal and/or breach acceptable use policies. This project is provided for educational purposes only. The author and contributors are not responsible for misuse.


---

Contributing

Contributions are welcome! If you want to:

Add threaded/async scanning

Add UDP scanning

Add output to file (CSV/JSON)

Add a CLI with argument parsing (e.g., argparse)


Open an issue or submit a pull request. Keep changes small and well-documented.


---

License

This project is provided under the MIT License — see LICENSE for details.


-

add argument parsing (so it can be run non-interactively),

or create a simple LICENSE file (MIT) and  .gitignore. Which one would you like next?
