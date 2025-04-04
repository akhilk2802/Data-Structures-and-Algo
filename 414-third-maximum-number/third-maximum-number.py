class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return max(nums)

        s = set(nums)
        sorted_s = sorted(s)
        if len(sorted_s) < 3:
            return sorted_s[-1]
        return sorted_s[-3]



