
def sum_of_odd_numbers(numbers):
    return sum(n for n in numbers if n % 2 != 0)


def main():
    print(sum_of_odd_numbers([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
