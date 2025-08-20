# Analysis
# Packet Analysis — 2025-08-20

## 🖥️ Capture Context
- **Interface:** Wi-Fi (host IP `192.168.0.185`)
- **Duration:** ~1 minute
- **Tool:** Wireshark v4.x
- **Generated Traffic:**
  - Visited `http://example.com`
  - Visited `https://www.wikipedia.org` and `https://msn.com`
  - Triggered DNS lookups for `example.com`

---

## 🔎 DNS Findings
- Multiple queries to `example.com`.
- Resolved addresses:
  - **IPv6 AAAA:** `2a01:860::1007`, `2a01:860::7`
  - **IPv4 A:** `2.207.183.7`, `2.207.183.135`
- Demonstrates that DNS can return multiple A/AAAA records, enabling redundancy/load balancing.
- Traffic is plaintext, so queries and answers are fully visible.

📸 *Reference:* `Screenshot 2025-08-20 160503.png`, `Screenshot 2025-08-20 160527.png`

---

## 🌐 HTTP Findings (plaintext)
- Captured a **GET /rootDesc.xml** request from host → router (`192.168.0.1`) with `HTTP/1.1 200 OK` response.
- Another GET request to `2.207.183.135` with plaintext headers and content type `(text/html)`.
- Full visibility of method, path, headers, and response codes.

📸 *Reference:* `Screenshot 2025-08-20 160719.png`

---

## 🔐 TLS/HTTPS Findings
- Captured **ClientHello** for `assets.msn.com`.
- Visible details:
  - **SNI:** `assets.msn.com`
  - **Supported TLS versions:** 1.3 and 1.2
  - **Cipher suites:** multiple advertised
  - **Extensions:** OCSP status request, signature algorithms, session ticket, supported groups
- Payload (web page content) remained **encrypted** — not visible in Wireshark.

📸 *Reference:* `Screenshot 2025-08-20 160617.png`

---

## 📌 Key Takeaways
1. **DNS** queries leak browsing intentions (hostnames) unless encrypted with DoH/DoT.
2. **HTTP** traffic is insecure: anyone on the path can read/modify requests and responses.
3. **HTTPS** secures content, but metadata (IP addresses, SNI, timing) is still observable.
4. Wireshark filters (`dns`, `http`, `tls`, `ip.addr == <host>`) make analysis focused and efficient.

---

## ✅ Conclusion
This capture exercise demonstrated the **contrast between plaintext protocols (DNS, HTTP)** and **encrypted protocols (HTTPS/TLS)**.  
It highlights why HTTPS adoption is critical, while also showing that metadata can still provide insights to defenders (or attackers).  
