class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        
        prefix1 = [0] * cols
        prefix2 = [0] * cols
        
        prefix1[0] = grid[0][0]
        for i in range(1, cols):
            prefix1[i] = prefix1[i - 1] + grid[0][i]
        
        prefix2[0] = grid[1][0]
        for i in range(1, cols):
            prefix2[i] = prefix2[i - 1] + grid[1][i]
        
        result = float('inf')
        for j in range(cols):
        
            top_right = prefix1[-1] - prefix1[j]
            bottom_left = prefix2[j - 1] if j > 0 else 0
            player2_score = max(top_right, bottom_left)
            result = min(result, player2_score)

        return result