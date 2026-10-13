
def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def main():
    arrays = [
        [1, 2, 3, 4],
        [1, 2, 3, 1],
        [],
        [1]
    ]
    for arr in arrays:
        print(f"{arr} -> {contains_duplicate(arr)}")


if __name__ == "__main__":
    main()
