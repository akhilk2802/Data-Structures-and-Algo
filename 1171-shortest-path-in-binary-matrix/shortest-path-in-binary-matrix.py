class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # validate
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        # BFS
        q = deque([(0, 0, 1)])

        dir = [(-1,0), (1,0), (0, 1), (0, -1), (-1,-1), (-1, 1), (1, -1), (1, 1)]

        while q:
            r, c, p = q.popleft()

            for nr, nc in dir:
                nnr, nnc = nr + r, nc + c

                if (r, c) == (rows - 1, cols - 1):
                    return p

                if 0 <= nnr < rows and 0 <= nnc < cols and visited[nnr][nnc] == False and grid[nnr][nnc] == 0:
                    visited[nnr][nnc] = True
                    q.append((nnr, nnc, p + 1))

        return -1