class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for x, y in directions:
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and (nx, ny) not in visited:
                    dfs(nx, ny)
        
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count