class Solution:
    def scoreOfString(self, s: str) -> int:

        diffArray = []

        for i in range(len(s) - 1):
            char1 = s[i]
            char2 = s[i + 1]
            ascii1 = ord(char1)
            ascii2 = ord(char2)
            diff = abs( ascii1 - ascii2 )
            diffArray.append(diff)

        return sum(diffArray)
