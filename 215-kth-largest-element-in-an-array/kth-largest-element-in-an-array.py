class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()
        print("nums -> ", nums)
        return nums[-k]