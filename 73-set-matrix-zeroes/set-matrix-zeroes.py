class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        print("rows -> ", rows)
        print("cols -> ", cols)

        for i in range(m):
            for j in range(n):
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0