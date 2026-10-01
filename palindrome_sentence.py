
def palindrome_sentence(sentence):
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    print(palindrome_sentence('A man, a plan, a canal, Panama'))

if __name__ == "__main__":
    main()
