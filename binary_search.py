
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    nums = [1, 3, 5, 7, 9, 11, 13]
    for target in [7, 2, 13, 1, 14]:
        print(f"Searching {target} -> {binary_search(nums, target)}")


if __name__ == "__main__":
    main()
