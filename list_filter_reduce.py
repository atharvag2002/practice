
from functools import reduce

def product_of_evens(numbers):
    evens = filter(lambda x: x % 2 == 0, numbers)
    return reduce(lambda a, b: a * b, evens, 1)


def main():
    print(product_of_evens([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()
