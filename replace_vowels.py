
def replace_vowels(text, symbol='*'):
    vowels = set('aeiouAEIOU')
    return ''.join(symbol if ch in vowels else ch for ch in text)


def main():
    print(replace_vowels('hello world'))

if __name__ == "__main__":
    main()
