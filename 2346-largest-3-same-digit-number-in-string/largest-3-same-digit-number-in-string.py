class Solution:
    
    def largestGoodInteger(self, num: str) -> str:

        best = ''
        r = 2

        while r < len(num):
            if num[r] == num[r - 1] == num[r - 2]:
                if best == '':
                    best = 0
                best = str(max(int(best), int(num[r])))
            r += 1

        print("best -> ", best)
        if best:
            return 3 * best
        return ""
