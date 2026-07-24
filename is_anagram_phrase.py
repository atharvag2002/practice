
def is_anagram_phrase(a, b):
    normalize = lambda text: ''.join(sorted(ch.lower() for ch in text if ch.isalnum()))
    return normalize(a) == normalize(b)


def main():
    print(is_anagram_phrase('Dormitory', 'Dirty room'))

if __name__ == "__main__":
    main()