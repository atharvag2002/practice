
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums


def main():
    arrays = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0, 0, 1, 1, 2, 2]
    ]
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Sorted: {sort_colors(arr.copy())}")


if __name__ == "__main__":
    main()
