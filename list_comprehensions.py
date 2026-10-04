
def squares(numbers):
    return [n * n for n in numbers]


def even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]


def main():
    values = list(range(1, 11))
    print("Squares:", squares(values))
    print("Evens:", even_numbers(values))


if __name__ == "__main__":
    main()
