class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return 1
            
        dp = [1] * n
        count = [1] * n 
        m = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
            m = max(m, dp[i])

        print("m : ", m)
        print("NUMS : ", nums)
        print("DP : ", dp)
        print("COUNT : ", count)

        return sum(c for l, c in zip(dp, count) if l == m)