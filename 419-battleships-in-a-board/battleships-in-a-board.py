class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        count = 0
        # Loop over rows and columns
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check if current cell is part of a battleship
                if board[i][j] == "X":
                    # Check if it's the beginning of a new battleship
                    if (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                        count += 1
        
        return count

        # count = 0
        # m, n = len(board), len(board[0])
        # visited = [[False for i in range(n)] for j in range(m)]
        # print("visited -> ", visited)

        # def dfs(r, c):




        # for i in range(m):
        #     for j in range(n):
        #         if dfs(i, j):
        #             count += 1

        # return count
