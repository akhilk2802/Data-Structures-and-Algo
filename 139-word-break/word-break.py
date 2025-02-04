class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for r in range(1, n+1):
            for j in range(r):
                if dp[j] and s[j:r] in wordDict:
                    dp[r] = True
                    break

        return dp[n]