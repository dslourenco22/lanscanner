
# LAN Scanner using ARP Requests

This Python script scans your local network using ARP requests to identify active devices. It uses `scapy` for packet crafting and `netifaces` to auto-detect the local subnet.

## Features

- Auto-detects the default network CIDR
- Sends ARP requests to discover devices on the LAN
- Displays IP address, MAC address, and hostname
- Customizable timeout for ARP replies
- Simple command-line interface

## Requirements

Install the required Python packages:

```bash
pip install scapy netifaces
```

Note: This script must be run with root privileges to send ARP packets.

## Usage

```bash
sudo python lan_scanner.py [-n NETWORK_CIDR] [-t TIMEOUT]
```

### Options

| Option | Description |
|--------|-------------|
| `-n`, `--network` | Target network in CIDR format (e.g. `192.168.1.0/24`). If omitted, the script attempts to auto-detect your local subnet. |
| `-t`, `--timeout` | Timeout in seconds for ARP replies (default: `2`) |

### Example

```bash
sudo python lan_scanner.py -n 192.168.0.0/24 -t 3
```

## Output

The script prints a table of discovered devices:

```
Found 5 device(s) — scan time: 2.01s
IP               MAC               Hostname
------------------------------------------------------------
192.168.0.1      aa:bb:cc:dd:ee:ff router.local
192.168.0.101    11:22:33:44:55:66 laptop.local
...
```

## How It Works

- Uses `netifaces` to detect the default gateway interface and subnet
- Crafts ARP requests using `scapy` and sends them to all IPs in the subnet
- Collects responses and resolves hostnames using `socket.gethostbyaddr`
- Displays results in a clean, sorted table

## Notes

- Works only on IPv4 networks
- Requires root privileges to send raw packets
- Hostname resolution may fail for some devices (shown as blank)

## License

This project is open-source and available under the MIT License.
```

You can paste this directly into your `README.md` file. Let me know if you'd like to add installation steps for Windows or a troubleshooting section.
