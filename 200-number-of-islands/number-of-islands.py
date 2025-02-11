class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


        def bfs(sR, sC):
            q = deque([(sR, sC)])
            grid[sR][sC] = "0"

            while q:
                r, c = q.popleft()
                for dr, dc in dir:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count 