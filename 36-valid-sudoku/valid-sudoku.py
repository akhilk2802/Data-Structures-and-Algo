class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for i in range(9):
            for j in range(9):

                num = board[i][j]

                if num == ".":
                    continue

                if (num in row_set[i] or num in col_set[j] or num in box_set[(i // 3, j // 3)]):
                    return False

                row_set[i].add(num)
                col_set[j].add(num)
                box_set[(i // 3, j // 3)].add(num)

        return True