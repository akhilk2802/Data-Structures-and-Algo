class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        '''
        Binary search => 

        [-2, -1, -1, 1, 2, 3]
        [ 0,  1,  2, 3, 4, 5]
                     ^

        [-3,-2,-1,0,0,1,2]
        [-3,-2,0,0,0,1,2]
        [-3,-2,0,0,1,2,3]
        [-2, -1, -1, 1, 2, 3]

        '''

        l = 0
        r = len(nums) - 1
        firstNonNegative = len(nums)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= 0:
                firstNonNegative = mid
                r = mid - 1
            else:
                l = mid + 1
            
        # updateNums = nums[firstNonNegative:]
        # print("UpdatedNums : ", updateNums)

        left = firstNonNegative
        right = len(nums) - 1
        firstStrictlyPositive = len(nums)

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] > 0:
                firstStrictlyPositive = middle
                right = middle - 1
            else:
                left = middle + 1

        print("firstNonNegative : ", firstNonNegative)
        print("firstStrictlyPositive : ", firstStrictlyPositive)
        print("len of positive : ", len(nums) - firstStrictlyPositive)
        print("len of negative : ", firstNonNegative)
        pos_len = len(nums) - firstStrictlyPositive
        # if firstNonNegative == 0:
            # pos_len = 0
        neg_len = firstNonNegative

        return max(pos_len, neg_len)



        # count_pos = 0
        # count_neg = 0

        # for num in nums:
        #     if num < 0:
        #         count_neg += 1
        #     elif num > 0:
        #         count_pos += 1

        # # print("count negative and count positive : ", count_neg, count_pos)

        # return max(count_neg, count_pos)