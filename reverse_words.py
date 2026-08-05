
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())


def main():
    print(reverse_words('hello world'))

if __name__ == "__main__":
    main()
