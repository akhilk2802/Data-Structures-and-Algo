class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:


        '''
        more Optimisations - 

        with prefix sum - 
        
        '''
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        for index in range(n):
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]


                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            total_sum += difference_array[index]

        return k

        '''
        Lets Optimise the problem - 
        i can do something with prefix sum 
        prefixSum_nums = [2,2,4]
        
        my approach - 
        1. i will find the max element in nums
        2. with the queries, i will check the max window possible
        3. at some point if the max window covers all the elements 
        4. i will also have a variable to track the max val 
        5. if at some point i can cover all the elements in the nums and maxval is greater than or equal to the max element in the nums
        6. i will return i + 1
        '''

        # maxVal = max(nums)

        # left = len(nums) - 1
        # right = 0

        # for i in range(len(queries)):
        #     start, end, val = queries[i]

        #     if start <= left:
        #         left = start
        #     if end >= right:
        #         right = end
            
        #     maxVal -= val
        #     window = (right - left) + 1
        #     if maxVal <= 0 and window == len(nums):
        #         return i + 1

        # return -1

        
        '''
        brute force approach -> 
        based on the queries perform the operations on the nums 
        check if all the elemenst after each i is zero
        if not go to next
        '''

        # def isZero(nums):
            
        #     for num in nums:
        #         if num != 0:
        #             return False
        #     return True
        # k = 0

        # for i in range(len(queries)):

        #     start, end, val = queries[i]
        #     for i in range(start, end):
        #         if nums[i] != 0:
        #             nums[i] = nums[i] - val
        #     k += 1
        #     if isZero(nums[start:end]):
        #         return k

        # return -1