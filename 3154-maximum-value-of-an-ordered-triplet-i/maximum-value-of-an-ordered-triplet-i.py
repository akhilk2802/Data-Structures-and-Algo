class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        '''
        optimising further ->
        there's an observation to make here ->
        we need to maximize the left value and multiplication value

        '''

        left, diff, result = 0, 0, 0

        for n in nums:
            result = max(result, diff * n)
            diff = max(diff, left - n)
            left = max(left, n)

        return result
        
        '''
        optimised ->
        greedy solution -> 
        there's an observation to make here ->
        if we want to maximise the value, num[i] should be as maximum then required
        '''

        # max_val = 0
        # n = len(nums)

        # left = nums[0]
        # for j in range(1, n):
        #     if nums[j] > left:
        #         left = nums[j]
        #     for k in range(j+1, n):
        #         val = (left - nums[j]) * nums[k]
        #         max_val = max(max_val, val)

        # return max_val



        '''
        since the constraints are the way they are given, this can be solved with triple nested loops
        '''

        # max_val = float("-inf")
        # n = len(nums)

        # for i in range(n - 2):
        #     for j in range(i+1, n - 1):
        #         for k in range(j+1, n):
        #             val = ((nums[i] - nums[j]) * nums[k])
        #             max_val = max(max_val, val)

        # if max_val < 0:
        #     return 0

        # return max_val

