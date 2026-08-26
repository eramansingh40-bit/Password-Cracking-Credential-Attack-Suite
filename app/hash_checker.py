import hashlib


def create_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password, target_hash):
    password_hash = create_hash(password)

    return password_hash == target_hash


def dictionary_attack(wordlist_file, target_hash):

    attempts = 0

    with open(wordlist_file, "r") as file:

        for line in file:

            candidate = line.strip()

            if not candidate:
                continue

            attempts += 1

            if check_password(candidate, target_hash):
                return candidate, attempts

    return None, attempts
