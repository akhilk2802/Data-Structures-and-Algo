class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def generate(nums, index=0, current=[], result=None):
            if result is None:
                result = []
            
            if len(nums) == index:
                result.append(current[:])
                return result

            generate(nums, index + 1, current + [nums[index]], result)
            generate(nums, index + 1, current, result)

            return result

        res = []
        res = generate(nums, 0)
        return res

        