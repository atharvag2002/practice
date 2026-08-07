
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())


def main():
    text = "this is a sample sentence"
    print(capitalize_words(text))


if __name__ == "__main__":
    main()
