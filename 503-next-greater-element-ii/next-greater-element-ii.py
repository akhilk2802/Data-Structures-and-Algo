class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        m = {}
        stack = []
        n = len(nums)

        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i % n]:
                m[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
            
        while stack:
            m[stack.pop()] = -1

        return [m[i] for i in range(n)]