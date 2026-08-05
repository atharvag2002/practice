
def median_of_list(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2


def main():
    print(median_of_list([3, 1, 4, 2]))

if __name__ == "__main__":
    main()
