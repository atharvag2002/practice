
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])


def main():
    sentence = "Python makes it easy to write code"
    print(reverse_sentence(sentence))


if __name__ == "__main__":
    main()
