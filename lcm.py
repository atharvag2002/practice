
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def main():
    print(lcm(12, 18))
    print(lcm(0, 5))


if __name__ == "__main__":
    main()
