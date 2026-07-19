
def word_reverse(sentence):
    return ' '.join(word[::-1] for word in sentence.split())


def main():
    print(word_reverse('Python rocks'))

if __name__ == "__main__":
    main()
