class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        startChar = word[0]
        n = len(word)

        rows, cols = len(board), len(board[0])
        dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def dfs(row, col, visited, index):
            if index == n-1:
                return True
            visited.add((row, col))
            for dr, dc in dir:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if board[nr][nc] == word[index + 1]:
                        if dfs(nr, nc, visited, index + 1):
                            return True
            visited.remove((row, col))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == startChar:
                    visited = set()
                    if dfs(i, j, visited, 0):
                        return True

        return False