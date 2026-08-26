import itertools
import string

from app.hash_checker import check_password


def brute_force_simulation(target_hash, max_length=3):

    characters = string.ascii_lowercase

    attempts = 0

    for length in range(1, max_length + 1):

        for combination in itertools.product(characters, repeat=length):

            candidate = "".join(combination)

            attempts += 1

            if check_password(candidate, target_hash):
                return candidate, attempts

    return None, attempts
