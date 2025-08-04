# 🔍 Task 1: Local Network Port Scanning (Cyber Security Internship)

## 📝 Objective
Perform a basic network reconnaissance to identify open ports and services on devices in your **local network** using `Nmap`.

---

## 🛠 Tools Used
- **Nmap**: For scanning the network and identifying open TCP ports.
- **ifconfig**: To determine local IP and subnet range.
- *(Optional)* **Wireshark**: For analyzing packets during the scan.

---

## 🖥 System Info
- **Local IP**: `10.0.2.15`
- **Subnet Mask**: `255.255.255.0` → **CIDR**: `/24`
- **Network Range**: `10.0.2.0/24`

---

## 🚀 Commands Used

### 🔸 Step 1: Discover Network Range
```bash
ifconfig
-----------------------------------------------
| IP Address | Open Ports      | Services     |
| ---------- | --------------- | ------------ |
| 10.0.2.2   | 135/tcp         | msrpc        |
| 10.0.2.2   | 445/tcp         | microsoft-ds |
| 10.0.2.2   | 1001/tcp        | webpush      |
| 10.0.2.3   | 53/tcp          | domain       |
-----------------------------------------------

💡 Key Learnings
Understood CIDR, port scanning, and service identification.

Practiced basic cyber reconnaissance methodology.

🔐 Basic Security Analysis
Port 135 (msrpc) and 445 (microsoft-ds): These are Windows ports often targeted by malware (e.g., EternalBlue). Should be firewalled off from untrusted networks.

Port 1001 (webpush): Custom or misconfigured service. Should be investigated.

Port 53 (DNS): Common and essential, but if misconfigured, can be abused for DNS amplification attacks.

