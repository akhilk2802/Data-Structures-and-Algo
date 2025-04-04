class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [1] * len(nums)
        # print("LIS -> ", LIS)
        # max_length = 0

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    # max_length = max(max_length, LIS[i])

        return max(LIS)