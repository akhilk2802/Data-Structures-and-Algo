class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # longest = float("-inf")
        # memo = {}

        # def isPalindrome(paliString):
        #     l, r = 0, len(paliString) - 1
        #     while l < r:
        #         if paliString[l] == paliString[r]:
        #             l += 1
        #             r -= 1
        #         else:
        #             return False
        #     return True

        # def generate(index, s, st):
        #     nonlocal longest

        #     if (index, st) in memo:
        #         return memo[(index, st)]

        #     if index == len(s):
        #         if isPalindrome(st):
        #             return len(st)
        #         return 0

        #     include = generate(index+1, s, st + s[index])
        #     exclude = generate(index+1, s, st)

        #     memo[(index, st)] = max(include, exclude)
        #     return memo[(index, st)]

        # return generate(0, s, "")
        

        s1 = s[::-1]
        # print("reversed : ", s1)

        m, n = len(s), len(s1)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]