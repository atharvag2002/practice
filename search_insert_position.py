
def search_insert_position(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def main():
    print(search_insert_position([1, 3, 5, 6], 5))
    print(search_insert_position([1, 3, 5, 6], 2))

if __name__ == "__main__":
    main()
