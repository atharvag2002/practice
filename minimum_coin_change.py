
def min_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def main():
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0)
    ]
    for coins, amount in test_cases:
        print(f"Coins: {coins}, Amount: {amount} -> {min_coin_change(coins, amount)}")


if __name__ == "__main__":
    main()
