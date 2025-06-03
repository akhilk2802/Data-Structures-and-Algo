class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if 0 <= i-1 < r and 0 <= j-1 < c and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True