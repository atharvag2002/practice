
import string

def remove_punctuation(text):
    return ''.join(ch for ch in text if ch not in string.punctuation)


def main():
    print(remove_punctuation('Hello, world!'))

if __name__ == "__main__":
    main()
