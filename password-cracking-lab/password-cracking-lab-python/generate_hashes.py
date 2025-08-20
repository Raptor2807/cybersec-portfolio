#!/usr/bin/env python3
import argparse, pathlib, hashlib, bcrypt

def main():
    ap = argparse.ArgumentParser(description="Generate SHA-256 and bcrypt hashes from a wordlist.")
    ap.add_argument('--wordlist', required=True)
    ap.add_argument('--out-dir', default='hashes')
    ap.add_argument('--bcrypt-cost', type=int, default=12)
    args = ap.parse_args()

    words = [w.strip() for w in open(args.wordlist, encoding='utf-8') if w.strip()]
    out = pathlib.Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)

    with open(out/'sha256.txt','w') as s, open(out/'bcrypt.txt','w') as b:
        for w in words:
            s.write(hashlib.sha256(w.encode()).hexdigest() + "\n")
            b.write(bcrypt.hashpw(w.encode(), bcrypt.gensalt(rounds=args.bcrypt_cost)).decode() + "\n")

    print(f"Wrote {(out/'sha256.txt')} and {(out/'bcrypt.txt')} with {len(words)} entries.")

if __name__ == '__main__':
    main()
