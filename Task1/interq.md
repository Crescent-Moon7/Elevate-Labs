#  Interview Questions – Task 1: Network Reconnaissance with Nmap

---

## 1. What is an open port?

An **open port** is a network port that is actively listening for incoming connections. It allows communication between devices, but if misconfigured or unprotected, it can be a potential entry point for attackers.

---

## 2. How does Nmap perform a TCP SYN scan?

Nmap sends a **SYN** packet to the target port:
- If it receives a **SYN-ACK**, the port is **open**.
- If it gets a **RST**, the port is **closed**.
- If there’s no response or an ICMP error, the port is **filtered**.

This is called a **half-open scan** because the TCP handshake is not completed, making it stealthier.

---

## 3. What risks are associated with open ports?

- Exposure to **vulnerable or outdated services**
- **Brute-force attacks** on login-enabled services
- Possibility of **remote code execution**
- Attackers using open ports to **exfiltrate data** or establish **backdoors**

---

## 4. Explain the difference between TCP and UDP scanning.

| Feature       | TCP Scan                  | UDP Scan                       |
|---------------|---------------------------|--------------------------------|
| Protocol      | Connection-oriented       | Connectionless                 |
| Method        | Uses SYN/ACK/RST flags    | Sends empty or crafted UDP packets |
| Detection     | More accurate             | Less accurate; many ports appear closed due to filtering |
| Stealth       | Less stealthy             | More stealthy (but noisy logs) |
| Use Case      | Web, SSH, SMB services    | DNS, SNMP, TFTP, etc.          |

---

## 5. How can open ports be secured?

- **Disable unused services/ports**
- Use **firewalls** to restrict access
- Enable **authentication and encryption**
- Apply **regular updates** and **patches**
- Implement **port knocking** or **VPN access controls**

---

## 6. What is a firewall’s role regarding ports?

A **firewall** acts as a gatekeeper by:
- **Allowing or blocking ports/services** based on rules
- Protecting the internal network from **unauthorized access**
- Monitoring **inbound and outbound traffic** to enforce security policies

---

## 7. What is a port scan and why do attackers perform it?

A **port scan** is a method used to discover open, closed, or filtered ports on a host.

**Attackers use port scans to:**
- Map the target network
- Identify available services
- Plan and launch targeted attacks

---

## 8. How does Wireshark complement port scanning?

**Wireshark** is a packet analyzer that:
- **Captures Nmap traffic** in real-time
- Lets you inspect **individual packets** (SYN, ACK, RST)
- Helps detect **suspicious behavior**, analyze responses, and validate Nmap findings

---

