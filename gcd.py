
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def main():
    print(gcd(48, 18))
    print(gcd(101, 10))


if __name__ == "__main__":
    main()
