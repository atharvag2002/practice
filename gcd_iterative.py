
def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def main():
    pairs = [(48, 18), (101, 10), (17, 17), (0, 5)]
    for a, b in pairs:
        print(f"gcd({a}, {b}) = {gcd_iterative(a, b)}")


if __name__ == "__main__":
    main()
