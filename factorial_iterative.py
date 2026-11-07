
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    numbers = [0, 1, 5, 7, 10]
    for n in numbers:
        print(f"{n}! = {factorial_iterative(n)}")


if __name__ == "__main__":
    main()
