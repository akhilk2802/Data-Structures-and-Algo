class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        count = 0
        visited = set()
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(node):
            x, y = node
            visited.add(node)

            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] == "1":
                    new_node = (nx, ny)
                    dfs(new_node)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs((i, j))
                    count += 1

        return count