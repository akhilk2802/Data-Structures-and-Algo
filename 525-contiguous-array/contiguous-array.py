class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        preSum = [0] * (n)
        pre = 0
        maxLength = 0
        m = {0: -1}

        for i in range(n):
            if nums[i] == 0:
                pre -= 1
            else: 
                pre += 1
            
            if pre in m:
                maxLength = max(maxLength, i - m[pre])
            else:
                m[pre] = i
            
        return maxLength