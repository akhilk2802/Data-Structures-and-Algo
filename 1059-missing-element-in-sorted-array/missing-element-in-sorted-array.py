class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        '''
        integer array with unique numbers in it
        k -> integer
        return the kth missing from the array

        example -> 
        [5,[6], 7,[8] 9, 10], k = 2
        Should i assume theres gonna be a missing integer all the time ? No, return 0
        will there be any negative integers ? No
        Always sorted
        '''

        '''
        Approach 1 ->
        
        '''

        n = len(nums)

        for i in range(1, n):
            missed_gap = nums[i] - nums[i-1] - 1
            if missed_gap >= k:
                return nums[i - 1] + k
            k -= missed_gap
        return nums[n - 1] + k