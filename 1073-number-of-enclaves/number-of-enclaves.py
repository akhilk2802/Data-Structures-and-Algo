class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        count = 0
        if rows == 0 and cols == 0:
            return 
        
        def bfs(r, c):
            queue = deque([(r,c)])
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while queue:
                dr, dc = queue.popleft()
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                    grid[dr][dc] = 0

                    for nx, ny in directions:
                        queue.append((nx + dr, ny + dc))
            
        for i in range(rows):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][cols - 1] == 1:
                bfs(i, cols - 1)
        
        for j in range(cols):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[rows - 1][j] == 1:
                bfs(rows - 1, j)

        print("Grid: ", grid)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1

        return count