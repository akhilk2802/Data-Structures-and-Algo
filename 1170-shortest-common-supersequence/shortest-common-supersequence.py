class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # Step 1: Compute the LCS using Dynamic Programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # Match found
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Max of excluding one

        # Step 2: Build the SCS by merging both strings while following LCS
        i, j = m, n
        result = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  
                result.append(str1[i - 1])  # Common character, move diagonally
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  
                result.append(str1[i - 1])  # Take from str1
                i -= 1
            else:
                result.append(str2[j - 1])  # Take from str2
                j -= 1

        # Append remaining characters from str1 and str2
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1

        return "".join(result[::-1])