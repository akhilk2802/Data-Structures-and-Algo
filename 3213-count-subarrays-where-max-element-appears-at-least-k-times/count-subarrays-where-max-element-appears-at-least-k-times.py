class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        maxElement = max(nums)
        
        n = len(nums)
        result = 0
        countOfMaxEl = 0
        r = 0

        for l in range(n):
            while r < n and countOfMaxEl < k:
                if nums[r] == maxElement:
                    countOfMaxEl += 1
                r += 1

            if countOfMaxEl >= k:
                result += n - r + 1

            if nums[l] == maxElement:
                countOfMaxEl -= 1

        return result
