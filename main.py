from app.password_strength import analyze_password
from app.dictionary_generator import generate_dictionary
from app.hash_checker import create_hash, dictionary_attack
from app.brute_force import brute_force_simulation
from app.report import generate_report


def main():

    print("=" * 50)
    print("PASSWORD CRACKING & CREDENTIAL ATTACK SUITE")
    print("Educational Security Audit Simulator")
    print("=" * 50)

    password = input("\nEnter a TEST password: ")

    print("\n[1] Password Strength Analysis")

    strength = analyze_password(password)

    print(f"Length: {strength['length']}")
    print(f"Lowercase: {strength['lowercase']}")
    print(f"Uppercase: {strength['uppercase']}")
    print(f"Numbers: {strength['digits']}")
    print(f"Special characters: {strength['special']}")
    print(f"Estimated entropy: {strength['entropy']} bits")
    print(f"Strength: {strength['strength']}")

    print("\n[2] Generating Dictionary")

    words = [
        "admin",
        "password",
        "aman",
        "security",
        "kali",
        "welcome",
        "test"
    ]

    wordlist_file = "data/wordlist.txt"

    count = generate_dictionary(words, wordlist_file)

    print(f"Generated {count} dictionary candidates")
    print(f"Wordlist saved to: {wordlist_file}")

    print("\n[3] Generating Test Hash")

    target_hash = create_hash(password)

    print(f"SHA-256 Hash:")
    print(target_hash)

    print("\n[4] Dictionary Attack Simulation")

    dictionary_result = dictionary_attack(
        wordlist_file,
        target_hash
    )

    found_password, attempts = dictionary_result

    print(f"Attempts: {attempts}")

    if found_password:
        print(f"Password FOUND: {found_password}")
    else:
        print("Password NOT found in dictionary")

    print("\n[5] Brute-Force Simulation")

    print("Testing lowercase combinations up to length 3...")

    brute_result = brute_force_simulation(
        target_hash,
        max_length=3
    )

    brute_password, brute_attempts = brute_result

    print(f"Attempts: {brute_attempts}")

    if brute_password:
        print(f"Password FOUND: {brute_password}")
    else:
        print("Password NOT found")

    print("\n[6] Generating Security Report")

    report_file = "reports/audit_report.txt"

    risk = generate_report(
        password,
        strength,
        dictionary_result,
        brute_result,
        report_file
    )

    print(f"Risk Level: {risk}")
    print(f"Report saved to: {report_file}")

    print("\n========================================")
    print("AUDIT COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()
