class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        '''
        candies = [5, 8, 6], k = 3
        5, 5, 3, 5, 1

        brute force approach - divide the piles based on the size of the lowest pile 
        create sub piles - 5, 5, 3, 5, 1

        1. find lowest 
        2. divide how many i can get within the next ones and keep increasing the count 

        check the hints and understood what it means 
        '''

        l, r = 1, max(candies)
        result = 0

        while l <= r:
            mid = (l + r) // 2

            child_count = 0
            for pile in candies:
                child_count += pile // mid

            if child_count >= k:
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result



        

        '''
        Dumb Solution => 
        '''

        # lowest = min(candies)
        # count = 0

        # for candy in candies:
        #     val = candy // lowest
        #     if val == 1:
        #         count += 1
        #         k -= 1
        #     if k == 0:
        #         return lowest

        # return 0
        