class Solution:
    
    def largestGoodInteger(self, num: str) -> str:

        def compare(right):

            if num[right] == num[right - 1] == num[right - 2]:
                return True
            return False

        best = ''
        r = 2

        while r < len(num):
            if compare(r):
                if best == '':
                    best = 0
                best = str(max(int(best), int(num[r])))
            r += 1

        print("best -> ", best)
        if best:
            return 3 * best
        return ""
