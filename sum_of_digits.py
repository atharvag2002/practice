
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def main():
    numbers = [123, 4567, 0, -89, 99999]
    for num in numbers:
        print(f"Sum of digits of {num} = {sum_of_digits(num)}")


if __name__ == "__main__":
    main()
