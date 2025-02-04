class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        count1 = 0
        count0 = 0
        n = len(s)
        
        for ch in s:
            if ch == "1":
                count1 += 1
            if ch == "0":
                count0 += 1
                count0 = min(count0, count1)

        return count0