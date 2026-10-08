
def rotate_array(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


def main():
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, 3, 4, 5], 2),
        ([1], 0)
    ]
    for arr, k in test_cases:
        print(f"Original: {arr}, k={k}")
        print(f"Rotated: {rotate_array(arr.copy(), k)}")


if __name__ == "__main__":
    main()
