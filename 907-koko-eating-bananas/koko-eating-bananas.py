class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low < high:
            
            mid = (low + high) // 2

            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid

            if time <= h:
                high = mid
            else:
                low = mid + 1

        return low



