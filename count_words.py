
def count_words(text):
    words = [word.lower() for word in text.split() if word.isalpha() or word.isalnum()]
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def main():
    text = "This is a test. This test is only a test."
    counts = count_words(text)
    print("Word frequency:")
    for word, count in sorted(counts.items()):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
