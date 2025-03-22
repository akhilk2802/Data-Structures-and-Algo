class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        '''
        [1,2,1,1,2,1]
        map = {
        }
        '''



        
        stack = []
        mapping = {}
        n = len(nums)

        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                mapping[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)

        # print("maps => ", mapping)

        while stack:
            mapping[stack.pop()] = -1

        # print("maps => ", mapping)
        
        return [mapping[i] for i in range(n)]


        
