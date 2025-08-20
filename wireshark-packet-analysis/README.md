# Wireshark Packet Capture & Analysis

## 🎯 Project Goal
Capture and analyze **DNS**, **HTTP**, and **TLS/HTTPS** traffic on a local network.  
Demonstrate the difference between plaintext vs. encrypted protocols and practice using Wireshark filters.

---

## 🛠️ Environment
- **Tool:** Wireshark v4.x
- **System:** (fill in: Windows / Linux / macOS)
- **Capture file:** [`Capture.pcapng`](./captures/Capture.pcapng)  
- **Screenshots:** see `screenshots/` folder

---

## 📡 Steps Performed
1. Opened Wireshark and started capture on active network interface (`192.168.0.185`).
2. Generated traffic by:
   - Visiting `http://example.com` (plaintext HTTP)
   - Visiting `https://www.wikipedia.org` and `https://msn.com` (TLS/HTTPS)
   - Triggering DNS lookups (`example.com`)
3. Applied filters:
   - `dns` → show DNS queries and responses  
   - `http` → show HTTP GET/200 OK requests  
   - `tls` → show TLS handshakes (ClientHello, ServerHello)  
   - `ip.addr == 192.168.0.185` → isolate host traffic
4. Saved capture to `captures/Capture.pcapng`.
5. Took screenshots of DNS answers, HTTP exchanges, and TLS handshake.

---

## 🔍 Findings

### 🟣 DNS
- Queries to `example.com` resolved to both **IPv6 (AAAA)** and **IPv4 (A)** records:
  - `2a01:860::1007`  
  - `2a01:860::7`  
  - `2.207.183.7`  
  - `2.207.183.135`
- Shows how DNS resolves names to multiple IPs, across IPv4/IPv6.

📸 *Screenshot:* `screenshots/Screenshot 2025-08-20 160503.png`

---

### 🟢 HTTP (plaintext)
- Observed cleartext **GET /rootDesc.xml** and `HTTP/1.1 200 OK` response between `192.168.0.185` and `192.168.0.1`.
- Also saw requests to `2.207.183.135` with visible response headers/content type `(text/html)`.

📸 *Screenshot:* `screenshots/Screenshot 2025-08-20 160719.png`

---

### 🔵 TLS / HTTPS
- Captured **ClientHello** to `assets.msn.com`.
- Visible details:
  - SNI (Server Name Indication): `assets.msn.com`
  - Supported TLS versions: `1.3`, `1.2`
  - Cipher suites, extensions, signature algorithms
- Application data (actual page content) was **encrypted and not visible**, proving confidentiality.

📸 *Screenshot:* `screenshots/Screenshot 2025-08-20 160617.png`

---

## 📑 Key Takeaways
- **DNS** traffic is plaintext (unless DoH/DoT is used) and reveals queried domains and IPs.
- **HTTP** exposes full requests and responses, including headers and content.
- **HTTPS** secures content, but metadata (server name, IP, handshake details) remains visible.
- Wireshark filters (`dns`, `http`, `tls`, `ip.addr == X`) are essential for cutting through noise.

---

## 📂 Project Structure
wireshark-packet-analysis/

├── README.md # this file

├── captures/

│ └── Capture.pcapng # saved capture file


├── screenshots/

│ ├── Screenshot 2025-08-20 160503.png

│ ├── Screenshot 2025-08-20 160527.png

│ ├── Screenshot 2025-08-20 160617.png

│ └── Screenshot 2025-08-20 160719.png

└── reports/

└── analysis-2025-08-20.md

---

## ⚠️ Ethics & Safety
- Performed only on my own machine/network.
- No sensitive traffic shared publicly.  
- Capture file only contains demo HTTP/DNS/HTTPS examples.
