
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def main():
    print(sum_of_list([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
