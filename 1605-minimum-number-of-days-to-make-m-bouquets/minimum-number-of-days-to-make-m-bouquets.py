class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        while l <= r:
            mid = (l+r) // 2
            if self.canMakeBouquet(bloomDay, m, k, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def canMakeBouquet(self, bloomDay, m, k, day):
        count = 0
        bouquet = 0
        for d in bloomDay:
            if d <= day:
                count += 1
                if count == k:
                    bouquet += 1
                    count = 0
            else:
                count = 0
            if bouquet == m:
                return True

        return False   