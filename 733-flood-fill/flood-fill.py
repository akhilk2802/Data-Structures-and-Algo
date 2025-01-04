class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])

        startColor = image[sr][sc]

        if startColor == color :
            return image
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != startColor:
                return 

            image[r][c] = color

            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        dfs(sr, sc)
        return image