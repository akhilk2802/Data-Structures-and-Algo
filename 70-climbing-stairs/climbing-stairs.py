class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        # dp = [0] * (n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2

        prev = 1
        prev2 = 2

        for i in range(3, n+1):
            # dp[i] = dp[i-1] + dp[i-2]
            curi = prev2 + prev
            prev = prev2
            prev2 = curi

        return prev2