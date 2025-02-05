class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if k <= 1:
            return 0
        
        l, r, prod, count = 0, 0, 1, 0
        
        while r < n:
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            count += 1 + (r-l)
            r += 1

        return count