
def longest_word(sentence):
    return max(sentence.split(), key=len)


def main():
    print(longest_word('find the longest word'))

if __name__ == "__main__":
    main()
