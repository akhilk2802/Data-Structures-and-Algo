class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        i = 0
        
        for j in range (0, len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        