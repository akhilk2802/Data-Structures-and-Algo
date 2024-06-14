class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        snums = sorted(nums)
        c = 0
        h = snums[0]
        for i in range(1, len(snums)):
            if snums[i] <= h:
                c += h + 1 - snums[i]
                snums[i] = h + 1
            h = snums[i]
        return c