
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left


def main():
    arrays = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1, 2, 3, 4, 5]
    ]
    for arr in arrays:
        peak_idx = find_peak_element(arr)
        print(f"{arr} -> Peak at index {peak_idx}, value {arr[peak_idx]}")


if __name__ == "__main__":
    main()
