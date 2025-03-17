class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        '''
        nums = [7,2,5,10,8]
        k = 2
        brute force approach => 
        sort the array => 
        nums = [2,5,7,8,10]
        now i need to figure out the numbe of subarrays i need to make to create the largest sum 
        '''
        def canMin(mid):
            currentVal = 0
            kval = 1
            for num in nums:
                currentVal += num
                if currentVal > mid:
                    kval += 1
                    currentVal = num
            return kval <= k 


        m = 0
        totalVal = 0

        for num in nums:
            m = max(m, num)
            totalVal += num

        # print("total Val : ", totalVal)
        # print("m  : ", m)

        low = m
        high = totalVal

        while low < high:

            mid = (low + high) // 2
            if canMin(mid):
                high = mid
            else:
                low = mid + 1

        return low
