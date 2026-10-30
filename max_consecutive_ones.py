
def max_consecutive_ones(nums):
    max_count = current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


def main():
    arrays = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 0, 0],
        [1, 1, 1, 1]
    ]
    for arr in arrays:
        print(f"{arr} -> Max consecutive 1s: {max_consecutive_ones(arr)}")


if __name__ == "__main__":
    main()
