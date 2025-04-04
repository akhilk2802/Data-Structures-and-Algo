class Solution:
    def countSubstrings(self, s: str) -> int:

        def countPalindromes(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        total_count = 0

        for i in range(len(s)):
            
            # for odd count ->
            total_count += countPalindromes(s, i, i)

            # for even count ->
            total_count += countPalindromes(s, i, i+1)

        return total_count
        