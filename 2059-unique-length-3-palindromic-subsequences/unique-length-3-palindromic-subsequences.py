class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        result = 0
        unique = set(s)

        for c in unique:
            start = s.find(c)
            end = s.rfind(c)

            if start < end:
                result += len(set(s[start+1:end]))

        return result