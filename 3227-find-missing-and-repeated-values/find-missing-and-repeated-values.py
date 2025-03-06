class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        a = 0
        b = 0
        n = len(grid)
        m = {}
        total = 0

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
        print("m : ", m)
        print("sumOfN : ", sumOfN)
        print("total : ", total)

        b = sumOfN - (total - a)
        print("b : ", b)
        print("a : ", a)
        return [a, b]

        print("a : ", a)