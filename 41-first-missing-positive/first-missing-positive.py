class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(0, len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        
        return len(nums) + 1
        