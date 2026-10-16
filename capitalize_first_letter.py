
def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())


def main():
    strings = ["hello world", "python programming", "test string"]
    for s in strings:
        print(f"{s} -> {capitalize_first_letter(s)}")


if __name__ == "__main__":
    main()
