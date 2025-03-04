from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        number_of_oranges = 0
        m, n = len(grid), len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    number_of_oranges += 1

        if number_of_oranges == 0:
            return 0
        
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total_time = -1

        while queue:
            total_time += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in dir:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        number_of_oranges -= 1
                        queue.append((nx, ny))

        return total_time if number_of_oranges == 0 else -1
        
        

        

        queue = deque([start])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    number_of_oranges -= 1
                    queue.append((nx, ny))


        print("number of oranges after : ", number_of_oranges)
        print("total time taken : ", total_time)