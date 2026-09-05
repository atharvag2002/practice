
def palindrome_number(n):
    s = str(n)
    return s == s[::-1]


def main():
    print(palindrome_number(1221))
    print(palindrome_number(1234))

if __name__ == "__main__":
    main()
