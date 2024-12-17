class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        arr = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        sortedArr = sorted(arr)

        return sortedArr[len(arr)//2]