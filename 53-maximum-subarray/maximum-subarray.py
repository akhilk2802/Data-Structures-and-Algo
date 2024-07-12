class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num, num + current_sum)
            max_sum = max(current_sum, max_sum)
        return max_sum
        