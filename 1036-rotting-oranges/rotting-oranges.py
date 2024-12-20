from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Initialize BFS queue
        queue = deque()
        fresh_oranges = 0

        # Add all initially rotten oranges to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:  # Rotten orange
                    queue.append((i, j))
                elif grid[i][j] == 1:  # Fresh orange
                    fresh_oranges += 1

        # Edge case: No fresh oranges at all
        if fresh_oranges == 0:
            return 0

        # BFS Direction vectors (4 directions)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        minutes_passed = -1

        # BFS Process
        while queue:
            minutes_passed += 1
            # Process all current rotten oranges
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # Explore all 4 directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        # Rot the fresh orange
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))

        # If there are still fresh oranges left, return -1
        return minutes_passed if fresh_oranges == 0 else -1