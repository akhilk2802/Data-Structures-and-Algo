class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        count = 0
        n = len(nums)

        for i in range(n-2):
            j = i + 1
            k = i + 2

            if nums[i] + nums[k] == nums[j] / 2:
                count += 1


        return count