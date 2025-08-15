class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1: return True

        while n > 1:
            n = n / 4

        print("n => ", n)
        if n == 1:
            return True
        else: return False