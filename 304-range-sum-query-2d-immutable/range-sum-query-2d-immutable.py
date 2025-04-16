class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sumMatrix = [[0]*cols for _ in range(rows)]

        self.sumMatrix[0][0] = matrix[0][0]

        for i in range(1, len(matrix)):
            self.sumMatrix[i][0] = self.sumMatrix[i-1][0] + matrix[i][0]

        for j in range(1, len(matrix[0])):
            self.sumMatrix[0][j] = self.sumMatrix[0][j-1] + matrix[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                self.sumMatrix[i][j] = (
                    self.sumMatrix[i-1][j]
                  + self.sumMatrix[i][j-1]
                  - self.sumMatrix[i-1][j-1]
                  + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.sumMatrix:
            return 0

        res = self.sumMatrix[row2][col2]
        if row1 > 0:
            res -= self.sumMatrix[row1-1][col2]
        if col1 > 0:
            res -= self.sumMatrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            res += self.sumMatrix[row1-1][col1-1]
        return res


# [[3, 3, 1, 5, 6], 
#  [8, 11, 12, 17, 23], 
#  [6, 17, 29, 46, 69], 
#  [5, 22, 51, 97, 166], 
#  [5, 27, 78, 175, 341]]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)