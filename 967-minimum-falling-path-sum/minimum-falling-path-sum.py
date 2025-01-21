class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(row, col):
            if col < 0 or col >= cols:
                return float('inf')
            
            if row == rows - 1:
                return matrix[row][col]
            
            if (row, col) in dp:
                return dp[(row, col)]

            down = dfs(row + 1, col)
            left_diag = dfs(row + 1, col - 1)
            right_diag = dfs(row + 1, col + 1)

            dp[(row, col)] = matrix[row][col] + min(down, left_diag, right_diag)
            return dp[(row, col)]

        return min(dfs(0, col) for col in range(cols))
