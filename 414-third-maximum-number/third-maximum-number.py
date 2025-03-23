class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return max(nums)

        s = set(nums)
        sorted_s = sorted(s)
        # print("sorted_s : ", sorted_s)
        if len(sorted_s) < 3:
            return sorted_s[-1]
        return sorted_s[-3]



