class Solution:
    def minOperations(self, nums: List[int]) -> int:

        '''
        now lets start the problem -> 
        questions i have -> 
        1. am i supposed to start from the 0th element ? or can i start from anywhere randomly ?

        lets start with the brute force approach -> 
        i will start with the first three elements 
        [0,1,1,1,0,0] -> 3
        [1,0,0,1,0,0] -> 2
        [1,1,1,0,0,0] -> 3
        [1,1,1,1,1,1] -> 6
        the whole number should be 1 * len(nums)
        the value is 6 
        current value is 3

        the required value is 4
        the current val is 3
        [0,1,1,1] -> 3 
        [1,0,0,1] -> 2
        [1,1,1,0] -> 3
        [0,0,0,0] -> 0
        [1,1,1,0] -> 3
        [1,0,0,1] -> 2


        definetly a sliding window problem, but how do i do it with the queue ?
        lets start here -> 
        [0,1,1,1,0,0]
        prefixSum = [0,1,2,3,3,3]
        [1,0,0,1,0,0]
        prefixSum = [1,1,1,2,2,2]
        [1,1,1,0,0,0]
        prefixSum = [1,2,3,3,3,3]
        [1,1,1,1,1,1]
        prefixSum = [1,2,3,4,5,6]
        [1,1,1,1,1,1]
        [0,1,2,3,4,5]
         ^   ^

        queue -> 
        lets see what are the posibilities with using a queue ->

        '''
        n = len(nums)
        count = 0

        for i in range(n-2):
            if nums[i] == 0:
                count += 1
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]

        if nums[-1] == 1 and nums[-2] == 1:
            return count
        else:
            return -1
