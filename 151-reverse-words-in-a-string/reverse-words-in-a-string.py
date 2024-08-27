class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        words.reverse()

        rs = " ".join(words)
        return rs

