class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        n = len(nums)
        preSum = [0] * n
        pre = 0
        maxLength = 0
        m = {0: -1}

        for i in range(n):
            pre += nums[i]
            val = pre - k

            if val in m:
                maxLength = max(maxLength, i - m[val])

            if pre not in m:
                m[pre] = i
        return maxLength
        
        