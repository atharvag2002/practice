
def gcd_recursive(a, b):
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def main():
    print(gcd_recursive(48, 18))

if __name__ == "__main__":
    main()
