class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            mFish = 0
            while queue:
                i, j = queue.popleft()
                print("i and j : ", i, j)
                mFish += grid[i][j]
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and grid[ni][nj] != 0:
                        visited.add((ni, nj))
                        print("Max Fish : ", mFish)
                        queue.append([ni, nj])

            return mFish

        visited = set()
        m, n = len(grid), len(grid[0])
        dir = [(0,1), (0, -1), (1, 0), (-1, 0)]
        maxFish = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in visited:
                    maxFish = max(maxFish, bfs(i, j))


        return maxFish




        