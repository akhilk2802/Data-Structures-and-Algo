class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return r