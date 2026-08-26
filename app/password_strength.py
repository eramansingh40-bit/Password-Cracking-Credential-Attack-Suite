import math
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "admin",
    "admin123",
    "qwerty",
    "welcome",
    "test123"
}


def calculate_entropy(password):
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return round(len(password) * math.log2(pool_size), 2)


def analyze_password(password):

    length = len(password)

    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digits = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    entropy = calculate_entropy(password)

    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if lowercase:
        score += 1

    if uppercase:
        score += 1

    if digits:
        score += 1

    if special:
        score += 1

    if password.lower() in COMMON_PASSWORDS:
        score = 0

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return {
        "length": length,
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": special,
        "entropy": entropy,
        "strength": strength
    }
