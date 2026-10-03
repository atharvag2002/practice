
def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def main():
    numbers = [1, 3, 9, 27, 81, 0, -3, 10]
    for num in numbers:
        print(f"{num} -> {is_power_of_three(num)}")


if __name__ == "__main__":
    main()
