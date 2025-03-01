class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # Algo -> 
        # 1. do a dfs for each column at the top and return the minimum sum
        # 2. can use cache to make it faster 

        n = len(matrix)
        res = float("inf")
        cache = {}
        
        def dfs(r, c):

            if r == n:
                return 0
            if c < 0 or c == n:
                return float("inf")
            if (r, c) in cache:
                return cache[(r, c)]
            x = matrix[r][c] + min(dfs(r+1, c-1), dfs(r+1, c), dfs(r+1, c+1))
            cache[(r, c)] = x
            return x



        
        for c in range(n):
            res = min(res, dfs(0, c))

        return res


        