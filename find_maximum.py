
def find_maximum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value


def main():
    nums = [3, 7, 2, 9, 4]
    print("Maximum:", find_maximum(nums))


if __name__ == "__main__":
    main()
