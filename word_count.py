
def word_count(text):
    words = text.split()
    return {
        'words': len(words),
        'characters': len(text),
        'characters_no_spaces': len(text.replace(' ', ''))
    }


def main():
    text = "Count words in this sentence."
    print(word_count(text))


if __name__ == "__main__":
    main()
