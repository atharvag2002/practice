
def kth_smallest(numbers, k):
    sorted_nums = sorted(numbers)
    return sorted_nums[k-1] if 0 < k <= len(sorted_nums) else None


def main():
    print(kth_smallest([5, 1, 4, 2, 3], 3))

if __name__ == "__main__":
    main()
