#!/usr/bin/env python3
import argparse, pathlib, hashlib, bcrypt

def read_lines(p):
    return [x.strip() for x in open(p, encoding='utf-8') if x.strip()]

def main():
    ap = argparse.ArgumentParser(description="Dictionary cracking for SHA-256 and bcrypt hashes.")
    ap.add_argument('mode', choices=['sha256','bcrypt'])
    ap.add_argument('--hash-file', required=True)
    ap.add_argument('--wordlist', required=True)
    ap.add_argument('--out', default=None)
    args = ap.parse_args()

    hashes = read_lines(args.hash_file)
    words = read_lines(args.wordlist)

    cracked = {}
    if args.mode == 'sha256':
        wmap = {hashlib.sha256(w.encode()).hexdigest(): w for w in words}
        for h in hashes:
            if h in wmap:
                cracked[h] = wmap[h]
    else:
        for h in hashes:
            hb = h.encode()
            for w in words:
                if bcrypt.checkpw(w.encode(), hb):
                    cracked[h] = w
                    break

    lines = [f"{h}:{pw}" for h,pw in cracked.items()]
    if args.out:
        pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        open(args.out,'w').write("\n".join(lines) + ("\n" if lines else ""))

    print(f"Cracked {len(cracked)}/{len(hashes)}")
    for l in lines: print(l)

if __name__ == '__main__':
    main()
