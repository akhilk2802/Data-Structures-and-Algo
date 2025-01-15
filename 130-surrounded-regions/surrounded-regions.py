class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        if rows == 0 and cols == 0:
            return

        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                x, y = queue.popleft()
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                    board[x][y] = 'S'
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.append((x + dx, y + dy))
        
        for i in range(rows):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[rows - 1][j] == 'O':
                bfs(rows - 1, j)

        print("board: ", board)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'