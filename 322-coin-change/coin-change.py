class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        print("DP -> ", dp)
        if dp[amount] != float("inf"):
            return dp[amount]
        
        return -1