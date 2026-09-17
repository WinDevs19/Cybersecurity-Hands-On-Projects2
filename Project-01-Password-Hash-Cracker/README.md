# 🔐 Project 01 — Password Hash Cracker Tool

## 📌 Project Overview

This project demonstrates the development and use of a **Password Hash Cracker Tool** in a controlled cybersecurity lab environment.

The purpose of the project is to understand how password hashes can be analyzed and tested against candidate passwords, while demonstrating why weak passwords and poor credential-storage practices can create serious security risks.

The project also explores the defensive side of password security, including stronger password policies, modern password-hashing algorithms, salting, Multi-Factor Authentication (MFA), and credential monitoring.

> **Ethical Use Notice:** This project was created strictly for educational purposes and authorized security testing. It should only be used on systems, credentials, and data that you own or have explicit permission to test.

---

## 🎯 Objectives

The objectives of this project were to:

- Understand how password hashing works.
- Analyze password hashes in a controlled environment.
- Implement password-testing logic using Python.
- Explore dictionary and brute-force cracking concepts.
- Compare candidate password hashes against a target hash.
- Understand the security impact of weak passwords.
- Improve Python scripting and cybersecurity automation skills.
- Identify defensive controls that make credential attacks more difficult.

---

## 🛠️ Technologies & Concepts

| Technology / Concept | Purpose |
|---|---|
| Python | Development of the hash-cracking tool |
| Hash Functions | Understanding one-way password transformations |
| Dictionary Attacks | Testing candidate passwords from a predefined wordlist |
| Brute Force | Understanding systematic password guessing |
| Password Security | Evaluating the risks associated with weak credentials |
| Kali Linux | Controlled cybersecurity testing environment |
| Git & GitHub | Version control and project documentation |

---

## 🧠 How Password Hashing Works

Instead of storing passwords directly as plaintext, secure applications store a derived representation of the password.

When authentication occurs, the supplied password is processed using the appropriate password-hashing mechanism and securely compared against the stored value.

This project demonstrates an important security principle:

Hashing a password does not automatically guarantee that the credential is secure.

If a weak password is used, an attacker who obtains password-hash data may be able to recover the original password through offline guessing techniques.

---

## ⚙️ Project Methodology

### Step 1 — Prepare the Lab Environment

A controlled environment was prepared for testing the Password Hash Cracker Tool.

The required Python environment, sample hashes, and test wordlists were prepared before executing the tool.

---

### Step 2 — Obtain an Authorized Test Hash

Sample password hashes were generated specifically for testing.

No unauthorized credentials or production password databases were used during this project.

---

### Step 3 — Load Candidate Passwords

The tool processes candidate passwords from an authorized test wordlist.

Each candidate is processed using the appropriate hashing method.

---

### Step 4 — Compare Hash Values

The resulting candidate hash is compared against the target test hash.

Conceptually:

```text
Candidate Password
        ↓
 Hash Function
        ↓
Generated Hash
        ↓
Compare with Target Hash
        ↓
 Match / No Match
```

---

### Step 5 — Identify a Matching Candidate

When the generated hash matches the target hash, the tool identifies the corresponding test password.

This demonstrates why weak or predictable passwords remain vulnerable even when plaintext passwords are not directly stored.


## 🔍 Security Findings

The project demonstrates several important security observations.

### Weak Passwords Increase Risk

Short, predictable, reused, or commonly used passwords are significantly more susceptible to password-guessing attacks.

### Hashing Alone Is Not Enough

The security of stored credentials depends on more than simply applying a hash function.

Password storage should use algorithms specifically designed for password hashing with appropriate configuration and unique salts.

### Offline Attacks Are Important to Understand

If an attacker obtains password-hash data, password guesses may potentially be tested offline without repeatedly interacting with the authentication system.

This makes strong credential storage particularly important.

---

## 🛡️ Security Recommendations

Organizations can reduce password-related risk by:

- Enforcing strong password requirements.
- Preventing the use of known compromised passwords.
- Using unique salts.
- Using modern password-hashing approaches such as **Argon2id, bcrypt, scrypt, or appropriately configured PBKDF2**.
- Selecting appropriate work factors or cost parameters.
- Implementing Multi-Factor Authentication (MFA).
- Monitoring authentication activity for suspicious behavior.
- Applying rate limiting to online authentication attempts.
- Protecting credential databases with strict access controls.
- Resetting potentially compromised credentials.
- Revoking active sessions when account compromise is confirmed or strongly suspected.

---

## 🔵 SOC / Blue-Team Relevance

This project also connects password security to SOC operations.

A SOC analyst investigating potential credential compromise may correlate:

- Repeated authentication failures.
- Successful authentication following multiple failures.
- Logins from unusual devices or sources.
- Authentication outside established user patterns.
- MFA changes.
- Password-reset events.
- New session creation.
- Suspicious post-authentication activity.
- Abnormal endpoint or network behavior associated with the account.

The key lesson is that **one authentication anomaly does not necessarily prove compromise**.

Analysts should correlate identity, endpoint, network, and user-context telemetry to develop a defensible incident hypothesis.

---

## 📊 Skills Demonstrated

This project demonstrates practical experience in:

- Python scripting
- Password security
- Hash analysis
- Security testing methodology
- Cybersecurity lab environments
- Credential-security concepts
- Security documentation
- Risk analysis
- Defensive security thinking
- SOC investigation methodology

---

## 💡 Key Takeaway

The most important lesson from this project is that password security depends on multiple layers of protection.

Strong passwords, secure password-hashing mechanisms, unique salts, appropriate cost parameters, MFA, monitoring, and effective incident response all contribute to protecting user credentials.

From a security analyst perspective, understanding how credential attacks work also improves the ability to recognize and investigate indicators of account compromise.
## 🧪 Successful Lab Test

The Password Hash Cracker Tool was tested in a controlled and authorized lab environment using a SHA-256 hash generated from a known test password.

### Test Configuration

- Algorithm: SHA-256
- Attack Method:Dictionary-based hash comparison
- Test Environment: Controlled lab
- Wordlist: `wordlist.txt`

### Execution Result

```text
=======================================================
       PASSWORD HASH CRACKER - EDUCATIONAL LAB
=======================================================
[+] Algorithm: SHA256
[+] Starting authorized hash test...

[+] MATCH FOUND
[+] Password: security2026
[+] Attempts: 3
```

### Result Analysis

The tool successfully identified the test password after 3 candidate attempts, confirming that the hash-comparison logic was functioning correctly.

This demonstrates how passwords that appear in predictable wordlists can potentially be recovered when an attacker obtains an unsalted fast hash.

> All hashes, passwords, and wordlists used in this demonstration were created specifically for this authorized educational lab.
---

## ⚠️ Disclaimer

This repository is intended solely for 
cybersecurity education, research, and authorized security testing.

Do not use the techniques or code contained in this project against credentials, accounts, applications, or systems without explicit authorization.

---

## 👤 Author

Winner Emmanuel Eyo

Cybersecurity | SOC Analysis | Incident Response | Penetration Testing

---

⭐ If you found this project useful, feel free to explore the other cybersecurity projects in this repository.
