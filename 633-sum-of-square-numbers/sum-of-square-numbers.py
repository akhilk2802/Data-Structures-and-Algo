import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(c ** 0.5) 

        while start <= end:
            k = (start * start) + (end * end)
            if k == c:
                return True
            elif k > c:
                end -= 1
            else:
                start += 1
        return False
        