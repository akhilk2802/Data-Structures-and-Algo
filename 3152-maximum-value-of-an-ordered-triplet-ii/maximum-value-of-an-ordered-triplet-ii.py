class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        diff = 0
        result = 0
        left = 0
        
        for n in nums:
            result = max(result, diff * n)
            diff = max(diff, left - n)
            left = max(left, n)
        return result