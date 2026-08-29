
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    test_cases = [(10, 2), (20, 4), (10, 0), (7, 3)]
    for a, b in test_cases:
        try:
            result = divide_numbers(a, b)
            print(f"{a} / {b} = {result}")
        except ValueError as e:
            print(f"{a} / {b} -> Error: {e}")


if __name__ == "__main__":
    main()
