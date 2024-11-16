class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        result = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        print(nums)
        
        for i in range(0, len(nums)):
            if nums[i] != i+1:
                result.append(i+1)

        return result