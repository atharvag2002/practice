
def vowel_consonant_count(text):
    vowels = set('aeiouAEIOU')
    vowel_count = sum(1 for ch in text if ch.isalpha() and ch in vowels)
    consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
    return vowel_count, consonant_count


def main():
    print(vowel_consonant_count('Hello World'))

if __name__ == "__main__":
    main()
