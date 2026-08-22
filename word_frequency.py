
def word_frequency(text):
    frequency = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def main():
    print(word_frequency('one two one three two one'))

if __name__ == "__main__":
    main()
