
def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in text if ch in vowels)


def main():
    examples = ["hello", "rhythm", "AEIOU", "Beautiful day"]
    for example in examples:
        print(f"{example!r} -> {count_vowels(example)} vowels")


if __name__ == "__main__":
    main()
