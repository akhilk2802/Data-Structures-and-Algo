class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        subsets = []

        def generateSubsets(nums, current, index):

            if index == len(nums):
                subsets.append(current[:])
                return subsets

            generateSubsets(nums, current + [nums[index]], index + 1)
            generateSubsets(nums, current, index + 1)

            return subsets


        subsets = generateSubsets(nums, [], 0)
        total = 0

        for i in range(len(subsets)):
            total_i = 0
            for j in range(len(subsets[i])):
                total_i ^= subsets[i][j]
            total += total_i
        
        return total
