class Solution:
    def coloredCells(self, n: int) -> int:
        
        val = (n*n) + ((n-1)*(n-1))
        return val