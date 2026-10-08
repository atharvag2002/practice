
def longest_palindrome_substring(s):
    best = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            fragment = s[i:j]
            if fragment == fragment[::-1] and len(fragment) > len(best):
                best = fragment
    return best


def main():
    print(longest_palindrome_substring('babad'))

if __name__ == "__main__":
    main()
