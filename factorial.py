
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    for value in [0, 1, 5, 7]:
        print(f"{value}! = {factorial_iterative(value)}")
        print(f"{value}! (recursive) = {factorial_recursive(value)}")


if __name__ == "__main__":
    main()
