
def digit_sum(n):
    return sum(int(ch) for ch in str(abs(n)))


def main():
    print(digit_sum(12345))

if __name__ == "__main__":
    main()
