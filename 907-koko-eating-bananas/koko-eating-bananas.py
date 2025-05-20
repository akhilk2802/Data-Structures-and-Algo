class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        I want to understand the thought process right, this is one of the craziest algorithms
        """

        def canFinish(value):

            req_hour = 0
            for i in range(len(piles)):
                req_hour += math.ceil(piles[i] / value)
            
            return req_hour <= h

        low = 1
        high = max(piles)

        while low <= high:

            mid = (low + high) // 2
            if canFinish(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low




