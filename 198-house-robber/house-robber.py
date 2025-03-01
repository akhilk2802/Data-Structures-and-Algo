class Solution:
    def rob(self, nums: List[int]) -> int:

        # algo - 
        # 1. keep a track of total value after stealing each house in their respected order 
        # 2. return the max of last two elements in a dp array 
        # 3. this should be totally based on the number of houses

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3: 
            return max(nums[0] + nums[2], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        print("dp : ", dp)

        return dp[n-1]