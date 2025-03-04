class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        nums = sorted(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    prev[i] = j

        print("DP : ", dp)
        print("prev : ", prev)

        result = []
        max_length = max(dp)
        last = dp.index(max_length)

        while last != -1:
            result.append(nums[last])
            last = prev[last]

        print("Result : ", result)
        return result[::-1]
        