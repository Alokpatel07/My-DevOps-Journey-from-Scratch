# Networking Fundamentals Notes

## 1. OSI and TCP/IP Model
- **OSI Model (7 layers):**
  1. Physical Layer – cables, switches, signals.
  2. Data Link Layer – MAC addresses, Ethernet.
  3. Network Layer – IP addresses, routing.
  4. Transport Layer – TCP, UDP (ensures delivery).
  5. Session Layer – manages sessions between apps.
  6. Presentation Layer – data format, encryption, compression.
  7. Application Layer – user-facing protocols (HTTP, DNS, etc.).

- **TCP/IP Model (4 layers):**
  1. Network Access Layer – physical + data link.
  2. Internet Layer – IP, routing.
  3. Transport Layer – TCP, UDP.
  4. Application Layer – HTTP, FTP, DNS, etc.

👉 TCP/IP is a simplified practical model, OSI is more theoretical.

---

## 2. IP Addresses, Subnets, and Ports
- **IP Address:** A unique number to identify devices (IPv4: 32-bit, IPv6: 128-bit).
- **Subnet:** Divides a network into smaller parts for efficiency and security.
  - Example: `192.168.1.0/24` means 256 IPs (192.168.1.0 – 192.168.1.255).
- **Port:** A number to identify specific processes/services on a device.
  - Example: HTTP → port 80, HTTPS → port 443, SSH → port 22.

---

## 3. DNS, DHCP, NAT Basics
- **DNS (Domain Name System):** Converts domain names (google.com) into IP addresses.
- **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses to devices.
- **NAT (Network Address Translation):** Allows private IPs to access the internet using a public IP.

---

## 4. HTTP/HTTPS, TCP, UDP Protocols
- **HTTP:** Unsecure web communication protocol (port 80).
- **HTTPS:** Secure HTTP using SSL/TLS (port 443).
- **TCP:** Reliable, connection-oriented protocol (ensures data delivery). Example: web browsing, email.
- **UDP:** Faster, connectionless protocol (no guarantee of delivery). Example: video streaming, gaming.

---

## 5. SSL/TLS Termination
- **SSL/TLS:** Encrypts communication between client and server.
- **Termination:** Process where encrypted traffic is decrypted at load balancer or proxy before reaching backend servers.

---

## 6. SSH, Secure Connections, Firewalls, Load Balancing, Proxy
- **SSH (Secure Shell):** Secure remote login (port 22).
- **Firewalls:** Control traffic using rules (block/allow IPs, ports, protocols).
- **Load Balancing:** Distributes traffic across multiple servers to ensure high availability and performance.
- **Proxy:** An intermediary server between client and internet (can cache, filter, or secure traffic).

---

## 7. Troubleshooting Commands
- **ping:** Tests connectivity between two devices.
- **curl:** Fetches data from URLs (test APIs, websites).
- **netstat:** Shows active network connections and listening ports.
- **traceroute (tracert on Windows):** Shows path packets take to a destination.

---

✅ These are the core networking fundamentals you should know for cloud, DevOps, and system admin roles.
