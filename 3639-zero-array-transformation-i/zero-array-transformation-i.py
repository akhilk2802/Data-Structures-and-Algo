class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        '''
        very beautiful problem - look up difference array for range update / delete
        '''

        n = len(nums)
        d_array = [0] * (n + 1)

        for i in range(len(queries)):
            l, r = queries[i]

            d_array[l] += 1
            d_array[r + 1] -= 1

        for i in range(1, len(d_array)):
            d_array[i] = d_array[i] + d_array[i-1]

        for i in range(n):
            if d_array[i] < nums[i]:
                return False

        return True
