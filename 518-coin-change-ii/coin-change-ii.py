class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def countWays(nums, index, T, dp):

            if index == 0:
                return 1 if T % nums[0] == 0 else 0

            if dp[index][T] != -1:
                return dp[index][T]

            exclude = countWays(nums, index - 1, T, dp)
            include = 0
            if nums[index] <= T:
                include = countWays(nums, index, T - nums[index], dp)

            dp[index][T] = include + exclude
            return dp[index][T]
        
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        return countWays(coins, len(coins)-1, amount, dp)
        