
def normalize(text):
    return ''.join(sorted(ch.lower() for ch in text if ch.isalnum()))


def are_anagrams(a, b):
    return normalize(a) == normalize(b)


def main():
    pairs = [
        ("listen", "silent"),
        ("triangle", "integral"),
        ("apple", "pale"),
        ("A gentleman", "Elegant man")
    ]

    for a, b in pairs:
        print(f"{a!r} and {b!r} are anagrams? {are_anagrams(a, b)}")


if __name__ == "__main__":
    main()
