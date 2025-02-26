class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        maxSum = float("-inf")
        currentSum = 0

        for num in nums:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        minSum = float("inf")
        currentMinSum = 0

        for num in nums:
            currentMinSum = min(num, currentMinSum + num)
            minSum = min(minSum, currentMinSum)

        print("minSum : ", minSum)

        return max(abs(minSum), maxSum)