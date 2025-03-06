class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        a, b, total = 0, 0, 0
        n = len(grid)
        seen = set()

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                total += val
                if val not in seen:
                    seen.add(val)
                else:
                    a = val
        N = n**2
        sumOfN = int(N*((N+1)/2))
        b = sumOfN - (total - a)
        
        return [a, b]