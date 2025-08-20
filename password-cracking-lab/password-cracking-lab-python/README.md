# 📄 Password Cracking Results — Python Lab

## 🔧 Setup

- **Date:** 2025-08-20
- **OS:** Ubuntu (WSL on Windows 11)
- **Python:** python3 --version
- **Libraries:** bcrypt vX.X

## 📝 Wordlist

- **File:** wordlists/demo.txt
- **Size:** X entries

Contents included:
```
password, password123, P@ssw0rd!, letmein, qwerty, ...
```

## 🔐 Hash Types Tested

- SHA-256 (fast, unsalted)
- bcrypt (salted, slow, cost=12)

## 🚀 Method

1. Generate demo hashes using `generate_hashes.py`.
2. Run `crack_hashes.py` with the demo wordlist.
3. Compare crack results for SHA-256 vs bcrypt.

## 📊 Results

### SHA-256
- Cracked: X / Y
- Example:
  ```
  <sha256hash>:password123
  <sha256hash>:letmein
  ```
- Time taken: ~instant

### bcrypt
- Cracked: X / Y
- Example:
  ```
  <bcrypt-hash>:P@ssw0rd!
  ```
- Time taken: noticeably slower (each check ~100ms+)

## 🔎 Analysis

- **SHA-256:** Extremely fast — dictionary cracked instantly.
- **bcrypt:** Much slower, resistant to brute-force. Salt ensures identical passwords have unique hashes.
- Even with small wordlists, bcrypt adds significant defense.

## ⚖️ Ethical Use

- All hashes were self-generated for lab/testing.
- No real user data was cracked.
- Intended for **education & portfolio** purposes only.

👉 When you run your actual scripts, just update:
- Date
- Python/bcrypt versions
- Number of cracked hashes
- Observed timings

---

# 📄 New README.md

# 🔐 Password Cracking Lab — Python Edition

This project demonstrates basic password cracking concepts using **Python**.  
It includes scripts to generate demo hashes (SHA-256 and bcrypt) and perform dictionary-based cracking.  
The focus is on **education, analysis, and ethical security testing**.

---

## 📂 Project Structure
```
password-cracking-lab-python/
├── generate_hashes.py     # Create SHA-256 & bcrypt hashes
├── crack_hashes.py        # Dictionary cracking for both formats
├── wordlists/
│   └── demo.txt           # Example wordlist
├── hashes/                # Generated hashes
├── reports/               # Results and analysis
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚡ Quick Start

### 1. Setup Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate Demo Hashes
```bash
python generate_hashes.py --wordlist wordlists/demo.txt --out-dir hashes --bcrypt-cost 12
```

This creates:
- `hashes/sha256.txt`
- `hashes/bcrypt.txt`

### 3. Crack Hashes
```bash
# SHA-256 (fast, unsalted)
python crack_hashes.py sha256 --hash-file hashes/sha256.txt --wordlist wordlists/demo.txt --out reports/cracked_sha256.txt

# bcrypt (slow, salted, cost=12)
python crack_hashes.py bcrypt --hash-file hashes/bcrypt.txt --wordlist wordlists/demo.txt --out reports/cracked_bcrypt.txt
```
