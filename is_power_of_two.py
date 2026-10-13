
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def main():
    print(is_power_of_two(16))
    print(is_power_of_two(18))

if __name__ == "__main__":
    main()
