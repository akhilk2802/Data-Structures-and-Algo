class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return
            
            backtrack(index + 1, current + [nums[index]])
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtrack(index + 1, current)

        backtrack(0, [])
        return result
