
import scapy.all as scapy
import socket
import argparse
import ipaddress
import time
import netifaces as ni

def detect_default_cidr():
    try:
        gw_iface = ni.gateways()['default'][ni.AF_INET][1]
        addr_info = ni.ifaddresses(gw_iface)[ni.AF_INET][0]
        ip = addr_info['addr']
        netmask = addr_info['netmask']
        network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
        return str(network)
    except Exception as e:
        print(f"Error detecting default CIDR: {e}")
        return None


def arp_scan(network_cidr, timeout=2):
    arp = scapy.ARP(pdst=network_cidr)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    ans, _ = scapy.srp(packet, timeout=timeout, verbose=False)
    devices = []
    for _, rcv in ans:
        ip = rcv.psrc
        mac = rcv.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = ""
        devices.append((ip, mac, hostname))
    return devices

def clean_print(devices, elapsed):
    if not devices:
        print("No devices found.")
        return
    print(f"Found {len(devices)} device(s) — scan time: {elapsed:.2f}s")
    print(f"{'IP':<16} {'MAC':<18} {'Hostname'}")
    print("-" * 60)
    for ip, mac, host in sorted(devices, key=lambda x: socket.inet_aton(x[0])):
        print(f"{ip:<16} {mac:<18} {host}")

def main():
    p = argparse.ArgumentParser(description="LAN Scanner using ARP requests (run as root)")
    p.add_argument("-n", "--network", help="Target network in CIDR (e.g. 192.168.1.0/24). If omitted, tries to detect local /24.")
    p.add_argument("-t", "--timeout", type=int, default=2, help="ARP reply timeout seconds")
    args = p.parse_args()

    cidr = args.network
    if not cidr:
        cidr = detect_default_cidr()
    if not cidr:
        print("Could not auto-detect network. Provide -n NETWORK/CIDR.")
        return

    try:
        ipaddress.IPv4Network(cidr)
    except Exception:
        print("Invalid network CIDR:", cidr)
        return

    start = time.time()
    devices = arp_scan(cidr, timeout=args.timeout)
    elapsed = time.time() - start
    clean_print(devices, elapsed)

if __name__ == "__main__":
    main()
