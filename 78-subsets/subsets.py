class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def generate(nums, index, current):
            if len(nums) == index:
                result.append(current[:])
                return result
            
            generate(nums, index + 1, current + [nums[index]])
            generate(nums, index + 1, current)

            return result
            

            


        result = []
        result = generate(nums, 0, [])
        return result