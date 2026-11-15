
def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value


def main():
    nums = [3, 7, 2, 9, 4]
    print("Minimum:", find_minimum(nums))


if __name__ == "__main__":
    main()
