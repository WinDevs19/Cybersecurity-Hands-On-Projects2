"""
Password Hash Cracker Tool
Author: Winner Emmanuel Eyo

Educational cybersecurity project for testing password hashes
generated from authorized lab data.
"""

import hashlib
import argparse


SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def calculate_hash(password, algorithm):
    """Generate a hexadecimal hash for a candidate password."""
    hash_function = SUPPORTED_ALGORITHMS[algorithm]
    return hash_function(password.encode("utf-8")).hexdigest()


def crack_hash(target_hash, wordlist_path, algorithm):
    """Compare words from a local wordlist against an authorized test hash."""

    attempts = 0

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:

            for line in wordlist:
                candidate = line.strip()

                if not candidate:
                    continue

                attempts += 1
                candidate_hash = calculate_hash(candidate, algorithm)

                if candidate_hash.lower() == target_hash.lower():
                    return candidate, attempts

    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        return None, attempts

    return None, attempts


def main():

    parser = argparse.ArgumentParser(
        description="Educational password hash testing tool"
    )

    parser.add_argument(
        "--hash",
        required=True,
        help="Authorized test hash"
    )

    parser.add_argument(
        "--wordlist",
        required=True,
        help="Path to the local test wordlist"
    )

    parser.add_argument(
        "--algorithm",
        choices=SUPPORTED_ALGORITHMS.keys(),
        default="sha256",
        help="Hash algorithm (default: sha256)"
    )

    args = parser.parse_args()

    print("=" * 55)
    print("       PASSWORD HASH CRACKER - EDUCATIONAL LAB")
    print("=" * 55)
    print(f"[+] Algorithm: {args.algorithm.upper()}")
    print("[+] Starting authorized hash test...")

    password, attempts = crack_hash(
        args.hash,
        args.wordlist,
        args.algorithm
    )

    if password:
        print("\n[+] MATCH FOUND")
        print(f"[+] Password: {password}")
        print(f"[+] Attempts: {attempts}")
    else:
        print("\n[-] No matching password found.")
        print(f"[-] Candidates tested: {attempts}")


if __name__ == "__main__":
    main()
