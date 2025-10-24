# LAN Scanner (ARP)

A simple Python LAN scanner that discovers devices on a local network using ARP requests.  
The script reports IP address, MAC address, and hostname (if available). It can auto-detect the host network or accept a user-specified CIDR.

> **Warning / Ethics:** Only run this tool on networks you own or have explicit permission to scan.

---

## Features
- Auto-detects local network CIDR (using `netifaces`)
- Performs an ARP scan to discover devices
- Resolves reverse DNS hostnames where available
- Outputs results in a readable table with scan time

---

## Requirements
- Python 3.8+
- `scapy`
- `netifaces`
- (optional) `sudo` / root privileges to send ARP packets

---

## Installation
1. Clone or copy this repository folder to your machine.
2. Install dependencies:
```bash
pip3 install scapy netifaces
Usage
Run the script as root (required to send ARP packets):

Auto-detect network:

bash
Copy code
sudo python3 lanscanner.py
Specify a CIDR:

bash
Copy code
sudo python3 lanscanner.py -n 192.168.1.0/24
Options:

lua
Copy code
-n, --network   Target network in CIDR (e.g. 192.168.1.0/24)
-t, --timeout   ARP reply timeout seconds (default: 2)
Example Output
nginx
Copy code
Found 3 device(s) — scan time: 2.34s
IP               MAC                Hostname
------------------------------------------------------------
192.168.1.1      aa:bb:cc:dd:ee:ff  router.local
192.168.1.10     11:22:33:44:55:66  laptop
192.168.1.45     77:88:99:aa:bb:cc  printer
Notes & Troubleshooting
On macOS, Scapy’s routing/packet behavior can be unreliable. If auto-detect fails, pass -n <CIDR> manually.

If you see permission errors, ensure you run the script with sudo or as root.

ARP scanning only discovers devices on the same Layer‑2 network segment (same switch / Wi‑Fi AP). It will not find devices across routers.

Extending the Project
Ideas you can add:

OUI/vendor lookup for MAC → manufacturer

Lightweight port probes to guess device type

Save results to CSV or SQLite

Flask dashboard to visualize devices over time

Alerting for new/unexpected devices

License
This project is released under the MIT License. See LICENSE for details.

Contact
Created by Lourenco DaSilva — feel free to open issues or PRs.

Copy code






You said:
put all of this into one md file 


ChatGPT said:
Here’s the full content ready to save directly as a single README.md file:

md
Copy code
# LAN Scanner (ARP)

A simple Python LAN scanner that discovers devices on a local network using ARP requests.  
The script reports IP address, MAC address, and hostname (if available). It can auto-detect the host network or accept a user-specified CIDR.

> **Warning / Ethics:** Only run this tool on networks you own or have explicit permission to scan.

---

## Features
- Auto-detects local network CIDR (using `netifaces`)
- Performs an ARP scan to discover devices
- Resolves reverse DNS hostnames where available
- Outputs results in a readable table with scan time

---

## Requirements
- Python 3.8+
- `scapy`
- `netifaces`
- (optional) `sudo` / root privileges to send ARP packets

---

## Installation
1. Clone or copy this repository folder to your machine.
2. Install dependencies:
```bash
pip3 install scapy netifaces
Usage
Run the script as root (required to send ARP packets):

Auto-detect network:

bash
Copy code
sudo python3 lanscanner.py
Specify a CIDR:

bash
Copy code
sudo python3 lanscanner.py -n 192.168.1.0/24
Options:

lua
Copy code
-n, --network   Target network in CIDR (e.g. 192.168.1.0/24)
-t, --timeout   ARP reply timeout seconds (default: 2)
Example Output
nginx
Copy code
Found 3 device(s) — scan time: 2.34s
IP               MAC                Hostname
------------------------------------------------------------
192.168.1.1      aa:bb:cc:dd:ee:ff  router.local
192.168.1.10     11:22:33:44:55:66  laptop
192.168.1.45     77:88:99:aa:bb:cc  printer
Notes & Troubleshooting
On macOS, Scapy’s routing/packet behavior can be unreliable. If auto-detect fails, pass -n <CIDR> manually.

If you see permission errors, ensure you run the script with sudo or as root.

ARP scanning only discovers devices on the same Layer‑2 network segment (same switch / Wi‑Fi AP). It will not find devices across routers.

Extending the Project
Ideas you can add:

OUI/vendor lookup for MAC → manufacturer

Lightweight port probes to guess device type

Save results to CSV or SQLite

Flask dashboard to visualize devices over time

Alerting for new/unexpected devices

License
This project is released under the MIT License. See LICENSE for details.

Contact
Created by Lourenco DaSilva — feel free to open issues or PRs.
