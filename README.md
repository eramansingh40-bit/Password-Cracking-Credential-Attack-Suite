# Password Cracking & Credential Attack Suite

##  Password Security Audit & Cracking Simulator

A beginner-friendly cybersecurity project designed to demonstrate how weak passwords can be identified and tested in a **controlled and authorized laboratory environment**.

The project combines password strength analysis, dictionary generation, hash verification, controlled brute-force simulation, and automated security report generation.

>  **Ethical Use Disclaimer:** This project is intended only for educational purposes and authorized security testing. It does not target real accounts, systems, or credentials. All password testing should use test data created specifically for the lab.

---

##  Project Overview

Passwords are one of the most important components of authentication security. Weak or predictable passwords can increase the risk of:

* Account takeover
* Credential stuffing
* Brute-force attacks
* Unauthorized access
* Data breaches
* Privilege escalation

This project demonstrates the basic methodology used during a password security audit.

The application accepts a **test password**, analyzes its strength, creates a SHA-256 test hash, generates a custom dictionary, performs a controlled dictionary simulation, performs a limited brute-force simulation, and generates an audit report.

---

##  Project Objectives

The main objectives are:

1. Analyze password strength.
2. Estimate password entropy.
3. Generate custom password-testing dictionaries.
4. Generate and verify SHA-256 hashes.
5. Simulate dictionary-based password testing.
6. Demonstrate controlled brute-force testing.
7. Identify weak passwords.
8. Generate a security audit report.
9. Provide recommendations for improving authentication security.
10. Demonstrate basic red-team and blue-team concepts.

---

##  Features

### 1. Password Strength Analyzer

The analyzer checks:

* Password length
* Lowercase characters
* Uppercase characters
* Numbers
* Special characters
* Common-password patterns
* Estimated entropy

Example:

```text
Password: abc123

Strength: WEAK
```

Example of a stronger password:

```text
Password: T9#vLm7@Qx2!

Strength: STRONG
```

---

### 2. Dictionary Generator

The dictionary generator creates password candidates from predefined test words.

For example:

```text
admin
password
security
kali
```

The program creates variations such as:

```text
admin
admin123
admin1234
admin2026
Admin
Admin123
ADMIN
```

This demonstrates how predictable password variations can increase password-cracking risk.

---

### 3. Hash Generator and Checker

The project uses Python's `hashlib` library to create SHA-256 hashes for laboratory test passwords.

Example:

```text
Test Password
      ↓
SHA-256
      ↓
Password Hash
```

Candidate passwords can then be compared with the generated test hash.

---

### 4. Dictionary Attack Simulation

The application reads candidates from the generated wordlist and compares each candidate with the test hash.

Example:

```text
Candidate: admin
Match: NO

Candidate: password
Match: NO

Candidate: admin123
Match: YES
```

The program reports the number of candidates tested.

---

### 5. Controlled Brute-Force Simulation

The project includes a deliberately limited brute-force demonstration.

The simulator tests lowercase combinations up to a small configurable length.

Example:

```text
a
b
c
...
aa
ab
ac
...
abc
```

This demonstrates the concept of brute-force attacks without providing a practical tool for attacking real accounts.

---

### 6. Security Audit Report

After testing, the application generates:

```text
reports/audit_report.txt
```

The report contains:

* Password strength
* Password characteristics
* Estimated entropy
* Dictionary simulation result
* Brute-force simulation result
* Overall risk
* Security recommendations

---

#  Project Architecture

```text
                         ┌──────────────────┐
                         │   User / Analyst │
                         └────────┬─────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │   main.py           │
                       │ Main Controller     │
                       └─────────┬───────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
     ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
     │ Password       │ │ Dictionary     │ │ Hash           │
     │ Strength       │ │ Generator      │ │ Checker        │
     │ Analyzer       │ │                │ │                │
     └───────┬────────┘ └───────┬────────┘ └───────┬────────┘
             │                  │                  │
             └──────────────────┼──────────────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Attack Simulation   │
                     │                     │
                     │ Dictionary          │
                     │ Brute Force         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Security Analysis   │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Audit Report        │
                     │ reports/            │
                     └─────────────────────┘
```

---

#  Project Workflow

```text
START
  │
  ▼
Enter Test Password
  │
  ▼
Password Strength Analysis
  │
  ▼
Generate SHA-256 Test Hash
  │
  ▼
Generate Test Dictionary
  │
  ▼
Dictionary Attack Simulation
  │
  ▼
Controlled Brute-Force Simulation
  │
  ▼
Analyze Results
  │
  ▼
Generate Security Report
  │
  ▼
END
```

---

#  Project Structure

```text
Password-Cracking-Credential-Audit/
│
├── app/
│   ├── __init__.py
│   ├── password_strength.py
│   ├── dictionary_generator.py
│   ├── hash_checker.py
│   ├── brute_force.py
│   └── report.py
│
├── data/
│   ├── sample_words.txt
│   └── wordlist.txt
│
├── reports/
│   └── audit_report.txt
│
├── screenshots/
│   └── README.md
│
├── tests/
│   └── test_password_security.py
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

#  Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python 3   | Main programming language           |
| hashlib    | SHA-256 hash generation             |
| itertools  | Brute-force simulation              |
| string     | Character-set handling              |
| math       | Entropy calculation                 |
| pytest     | Automated testing                   |
| Linux/Kali | Development and testing environment |
| Git/GitHub | Version control and project hosting |

---

#  Installation

## 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Password-Cracking-Credential-Audit
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with your actual repository URL.

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

On Kali Linux/Ubuntu:

```bash
source venv/bin/activate
```

You should see:

```text
(venv)
```

in the terminal.

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

The current project uses Python standard-library modules, so there are no major external dependencies.

For testing:

```bash
pip install pytest
```

---

#  Running the Project

Run:

```bash
python3 main.py
```

The program will ask for a test password:

```text
Enter a TEST password:
```

Enter a password created specifically for your laboratory demonstration.

Example:

```text
admin123
```

---

#  Example Output

```text
==================================================
PASSWORD CRACKING & CREDENTIAL ATTACK SUITE
Educational Security Audit Simulator
==================================================

Enter a TEST password: admin123

[1] Password Strength Analysis

Length: 8
Lowercase: True
Uppercase: False
Numbers: True
Special characters: False
Estimated entropy: ...
Strength: WEAK

[2] Generating Dictionary

Generated dictionary candidates

[3] Generating Test Hash

SHA-256 Hash:
<generated hash>

[4] Dictionary Attack Simulation

Password FOUND: admin123

[5] Brute-Force Simulation

Testing lowercase combinations up to length 3...

[6] Generating Security Report

Risk Level: HIGH
Report saved to: reports/audit_report.txt

========================================
AUDIT COMPLETED
========================================
```

---

#  Sample Security Results

## Weak Password

```text
Password: admin123

Strength: WEAK
Dictionary Attack: FOUND
Risk Level: HIGH
```

Reason:

* Common word
* Predictable number suffix
* No uppercase characters
* No special characters
* Relatively short

---

## Strong Password

Example:

```text
T9#vLm7@Qx2!
```

Expected result:

```text
Strength: STRONG
Dictionary Attack: NOT FOUND
```

The password is more resistant because it has greater length and character diversity.

---

#  Automated Testing

The project includes unit tests in:

```text
tests/test_password_security.py
```

Run:

```bash
pytest
```

Expected output:

```text
============================= test session starts =============================

tests/test_password_security.py ....                         [100%]

============================== 4 passed ==============================
```

The tests verify:

* Weak password detection
* Strong password detection
* Hash creation
* Correct password/hash matching
* Incorrect password rejection

---

#  Audit Report

The application automatically creates:

```text
reports/audit_report.txt
```

The report contains:

```text
PASSWORD STRENGTH
DICTIONARY SIMULATION
BRUTE-FORCE SIMULATION
OVERALL RISK
RECOMMENDATIONS
```

Example:

```text
OVERALL RISK
------------------------------
Risk Level: HIGH

RECOMMENDATIONS
------------------------------
1. Use long and unique passwords.
2. Avoid common dictionary words.
3. Implement multi-factor authentication.
4. Implement login rate limiting.
5. Never reuse passwords.
6. Use secure password hashing mechanisms.
```

---

#  Security Recommendations

Based on the audit results, organizations should consider:

### Strong Password Policies

Use passwords/passphrases that are:

* Long
* Unique
* Difficult to predict
* Not based on common words
* Not reused between services

### Multi-Factor Authentication

MFA provides an additional security layer even when a password is compromised.

### Rate Limiting

Applications should limit repeated authentication attempts.

Example:

```text
Multiple failed attempts
          ↓
Rate limiting
          ↓
Temporary delay/block
          ↓
Alert security team
```

### Account Lockout / Detection

Repeated failed authentication attempts should be monitored and investigated.

### Secure Password Storage

Applications should never store passwords as plaintext.

Production authentication systems should use an appropriate password-hashing mechanism designed for password storage, with unique salts and suitable work factors.

---

#  Blue-Team Perspective

This project can also be used to understand defensive security.

A SOC analyst can monitor:

```text
Failed Login
     ↓
Repeated Attempts
     ↓
Possible Brute Force
     ↓
SIEM Alert
     ↓
Investigation
     ↓
IP/User Analysis
     ↓
Response
```

Possible defensive controls include:

* SIEM monitoring
* Authentication logging
* Rate limiting
* MFA
* Account lockout policies
* Password policies
* Alerting on repeated failures
* IP reputation monitoring

---

#  Red-Team Concepts Demonstrated

The project demonstrates the concepts of:

* Password dictionary attacks
* Password mutation
* Hash comparison
* Brute-force methodology
* Password predictability
* Password strength assessment

All testing is performed against **locally generated test data**.

---

#  Blue-Team Concepts Demonstrated

The project demonstrates:

* Password auditing
* Authentication security
* Weak-password identification
* Security recommendations
* Brute-force risk assessment
* Security reporting
* Automated testing

---

#  Learning Outcomes

After completing this project, the learner should understand:

1. How password strength can be evaluated.
2. Why predictable passwords are dangerous.
3. How password hashes can be compared with candidate passwords.
4. How dictionary attacks work conceptually.
5. How brute-force attacks work conceptually.
6. Why longer passwords are generally more resistant to guessing.
7. Why MFA is important.
8. Why authentication rate limiting is important.
9. How security audit reports are generated.
10. How password security relates to SOC operations.

---

# Recommended Screenshots

Add project evidence to the `screenshots/` directory.

Recommended screenshots:

```text
screenshots/
├── 01-project-structure.png
├── 02-program-start.png
├── 03-weak-password.png
├── 04-strong-password.png
├── 05-wordlist.png
├── 06-hash-generation.png
├── 07-dictionary-simulation.png
├── 08-bruteforce-simulation.png
├── 09-audit-report.png
└── 10-pytest-results.png
```

Do not include real passwords, credentials, or sensitive information in screenshots.

---

# Project Deliverables

The final submission contains:

* [x] Python application
* [x] Password strength analyzer
* [x] Dictionary generator
* [x] SHA-256 test hash generator
* [x] Dictionary attack simulator
* [x] Controlled brute-force simulator
* [x] Audit report generator
* [x] Automated tests
* [x] Project documentation
* [ ] Architecture diagram
* [ ] Screenshots
* [ ] Final PDF report
* [ ] Presentation/PPT

---

# Limitations

This is an **educational simulation**, not a production password-cracking platform.

Current limitations include:

* Uses locally generated test hashes.
* Does not target real authentication systems.
* Brute-force simulation is intentionally limited.
* Does not extract real Linux `/etc/shadow` credentials.
* Does not extract Windows SAM credentials.
* Does not perform online login attacks.
* Does not bypass authentication.
* Does not use stolen credentials.
* Does not demonstrate credential theft.

These limitations are intentional to keep the project suitable for a controlled cybersecurity laboratory.

---

# Ethical Disclaimer

This project must only be used for:

* Personal cybersecurity labs
* Authorized penetration testing
* Educational demonstrations
* Security research with permission
* Password-policy auditing

Never use this project to attack accounts, systems, services, or credentials without explicit authorization.

---

# Future Improvements

Possible future improvements include:

* GUI interface using Tkinter
* PDF report generation
* JSON report generation
* Password policy configuration
* More advanced entropy analysis
* Common-password database integration
* Login-failure log analysis
* SIEM integration
* Wazuh integration
* Splunk integration
* Brute-force detection rules
* Password-policy compliance scoring
* Interactive dashboard
* Docker deployment

---

# Author

**Amandeep Singh**

Cybersecurity / SOC Analyst Project

Focus Areas:

* SOC Operations
* Threat Detection
* SIEM
* Linux Security
* Authentication Security
* Python
* Cybersecurity Automation

---

# License

This project is intended for educational and authorized security-testing purposes.

Use responsibly and only against systems and data for which you have explicit permission.
