class Solution:
    def longestPalindrome(self, s: str) -> str:

        '''
        babad -> 5
        longest = 0
        dp = []

        cbbd 

        '''
        result = ""
        n = len(s)

        for i in range(n):
            l, r = i, i 
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                length = r - l + 1
                if length > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                length = r - l + 1
                if length > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
        
        return result