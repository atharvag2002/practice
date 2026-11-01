
def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def main():
    numbers = [0, 1, 5, 10, 20, 50]
    for n in numbers:
        print(f"fib({n}) = {fibonacci_dp(n)}")


if __name__ == "__main__":
    main()
