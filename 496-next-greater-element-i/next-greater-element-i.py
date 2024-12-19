class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        stack = []
        mapping = {}

        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)

        while stack:
            mapping[stack.pop()] = -1

        for n in nums1:
            ans.append(mapping[n])
        
        return ans

        