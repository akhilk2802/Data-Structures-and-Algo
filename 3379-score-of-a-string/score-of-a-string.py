class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0
        for i in range(len(s) - 1):
            ascii1 = ord(s[i])
            ascii2 = ord(s[i + 1])
            diff = abs( ascii1 - ascii2 )
            total += diff
        return total
