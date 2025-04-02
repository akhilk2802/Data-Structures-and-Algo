class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        '''
        since the constraints are the way they are given, this can be solved with triple nested loops
        '''

        max_val = float("-inf")
        n = len(nums)

        for i in range(n - 2):
            for j in range(i+1, n - 1):
                for k in range(j+1, n):
                    val = ((nums[i] - nums[j]) * nums[k])
                    max_val = max(max_val, val)

        if max_val < 0:
            return 0

        return max_val

