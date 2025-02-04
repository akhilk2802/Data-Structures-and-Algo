class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        n = len(nums)
        maxSum = 0
        sumSoFar = nums[0]

        if n == 1:
            return nums[0]

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                sumSoFar += nums[i]
                maxSum = max(sumSoFar, maxSum)
            else:
                maxSum = max(sumSoFar, maxSum)
                sumSoFar = nums[i]

        return maxSum