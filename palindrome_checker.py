
def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in str(text) if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    examples = ["racecar", "Madam", "Step on no pets", 121, 12321, 12345]
    for item in examples:
        print(f"{item!r} -> {is_palindrome(item)}")


if __name__ == "__main__":
    main()
