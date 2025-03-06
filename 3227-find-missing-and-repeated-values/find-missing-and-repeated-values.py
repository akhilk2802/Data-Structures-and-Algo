class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        a, b, total = 0, 0, 0
        n = len(grid)
        m = {}

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                total += val
                if val in m:
                    m[val] += 1
                    if m[val] == 2:
                        a = val
                else:
                    m[val] = 1
        N = n**2
        sumOfN = int(N*((N+1)/2))
        b = sumOfN - (total - a)
        
        return [a, b]