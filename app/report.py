def generate_report(
    password,
    strength_result,
    dictionary_result,
    brute_force_result,
    output_file
):

    dictionary_password, dictionary_attempts = dictionary_result
    brute_password, brute_attempts = brute_force_result

    if dictionary_password or brute_password:
        risk = "HIGH"
    elif strength_result["strength"] == "MEDIUM":
        risk = "MEDIUM"
    else:
        risk = "LOW"

    with open(output_file, "w") as file:

        file.write("=" * 50 + "\n")
        file.write("PASSWORD SECURITY AUDIT REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Password Tested: {password}\n\n")

        file.write("PASSWORD STRENGTH\n")
        file.write("-" * 30 + "\n")
        file.write(
            f"Length: {strength_result['length']}\n"
        )
        file.write(
            f"Lowercase: {strength_result['lowercase']}\n"
        )
        file.write(
            f"Uppercase: {strength_result['uppercase']}\n"
        )
        file.write(
            f"Numbers: {strength_result['digits']}\n"
        )
        file.write(
            f"Special Characters: {strength_result['special']}\n"
        )
        file.write(
            f"Estimated Entropy: {strength_result['entropy']} bits\n"
        )
        file.write(
            f"Strength: {strength_result['strength']}\n\n"
        )

        file.write("DICTIONARY SIMULATION\n")
        file.write("-" * 30 + "\n")

        if dictionary_password:
            file.write("Result: PASSWORD FOUND\n")
            file.write(f"Candidate: {dictionary_password}\n")
        else:
            file.write("Result: PASSWORD NOT FOUND\n")

        file.write(f"Attempts: {dictionary_attempts}\n\n")

        file.write("BRUTE-FORCE SIMULATION\n")
        file.write("-" * 30 + "\n")

        if brute_password:
            file.write("Result: PASSWORD FOUND\n")
            file.write(f"Candidate: {brute_password}\n")
        else:
            file.write("Result: PASSWORD NOT FOUND\n")

        file.write(f"Attempts: {brute_attempts}\n\n")

        file.write("OVERALL RISK\n")
        file.write("-" * 30 + "\n")
        file.write(f"Risk Level: {risk}\n\n")

        file.write("RECOMMENDATIONS\n")
        file.write("-" * 30 + "\n")
        file.write("1. Use long and unique passwords.\n")
        file.write("2. Avoid common dictionary words.\n")
        file.write("3. Use multi-factor authentication.\n")
        file.write("4. Implement login rate limiting.\n")
        file.write("5. Never reuse passwords.\n")
        file.write("6. Use secure password hashing mechanisms.\n")

    return risk
