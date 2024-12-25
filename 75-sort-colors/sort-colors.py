from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[mid] and nums[low]
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                # Swap nums[mid] and nums[high]
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                # nums[mid] == 1, just move mid forward
                mid += 1