class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        # Step 1: Initialize count = 0
        # Step 2: Loop through each row and column of the board
        # Step 2a: If current cell is '.', skip it
        # Step 2b: If the cell above exists and is 'X', skip (it's part of a vertical ship)
        # Step 2c: If the cell to the left exists and is 'X', skip (it's part of a horizontal ship)
        # Step 2d: Else, this is the start of a new ship → increment count
        # Step 3: Return the total count

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] == "X":
                    if (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                        count += 1
        return count
