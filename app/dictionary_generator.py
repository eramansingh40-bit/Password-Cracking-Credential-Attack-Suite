def generate_dictionary(words, output_file):
    candidates = set()

    for word in words:
        word = word.strip()

        if not word:
            continue

        variations = [
            word,
            word.lower(),
            word.upper(),
            word.capitalize(),
            word + "123",
            word + "1234",
            word + "2026",
            word.capitalize() + "123"
        ]

        for item in variations:
            candidates.add(item)

    with open(output_file, "w") as file:
        for candidate in sorted(candidates):
            file.write(candidate + "\n")

    return len(candidates)
