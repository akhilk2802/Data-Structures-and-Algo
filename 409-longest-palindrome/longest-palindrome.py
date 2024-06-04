class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = Counter(s)
        length = 0
        odd = False

        for count in freq.values():
            length += (count // 2 ) * 2
            if count % 2 == 1:
                odd = True
            
        if odd:
            length += 1

        return length