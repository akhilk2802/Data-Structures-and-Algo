class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHouse(arr):
            n = len(arr)

            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[0], arr[1])
            
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            # dp[2] = max(arr[0] + arr[2], arr[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])

            return dp[n-1]

    
        if len(nums) == 1: return nums[0]
        ans1 = robHouse(nums[1:])
        ans2 = robHouse(nums[:-1])

        return max(ans1, ans2)