class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        maxSum = float("-inf")
        currentSum = 0
        minSum = float("inf")
        currentMinSum = 0

        for num in nums:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
            currentMinSum = min(num, currentMinSum + num)
            minSum = min(minSum, currentMinSum)


        return max(abs(minSum), maxSum)