class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        print("Dp : ", dp)
        result = []
        val = max(dp)
        for i in range(len(dp)-1, -1, -1):
            if dp[i] == val:
                if len(result) == 0:
                    result.append(nums[i])
                if result[-1] > nums[i]:
                    result.append(nums[i])
                val -= 1
        
        print("Result : ", result)

        return max(dp)

