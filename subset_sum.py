
def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]


def main():
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9),
        ([3, 34, 4, 12, 5, 2], 30),
        ([1, 2, 3], 7)
    ]
    for nums, target in test_cases:
        print(f"Subset sum {target} in {nums} -> {subset_sum(nums, target)}")


if __name__ == "__main__":
    main()
