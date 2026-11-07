
def difference_of_squares(n):
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return abs(square_of_sum - sum_of_squares)


def main():
    numbers = [5, 10, 100]
    for n in numbers:
        print(f"n={n}: {difference_of_squares(n)}")


if __name__ == "__main__":
    main()
