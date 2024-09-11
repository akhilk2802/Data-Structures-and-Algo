class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) 
        while l < h:
            mid = (h+l) // 2

            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid
        return l
        