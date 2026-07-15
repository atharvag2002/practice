
def integer_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    print(integer_palindrome(121))
    print(integer_palindrome(123))

if __name__ == "__main__":
    main()
