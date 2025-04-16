class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in m:
                return [m[comp], i]
            m[nums[i]] = i

        return []