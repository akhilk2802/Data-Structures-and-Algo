class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        # print("isWater : ", isWater)
        
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
                    

        # print("isWater after adding to queue : ", isWater)
        # print("Queue: ", queue)

        dir = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            dr, dx = queue.popleft()
            curr_height = height[dr][dx]
            # print("dr, dx: ", dr, dx)
            for r, x in dir:
                nr, nx = dr + r, dx + x
                if 0 <= nr < rows and 0 <= nx < cols and height[nr][nx] == -1:
                    height[nr][nx] = curr_height + 1
                    queue.append((nr, nx))

        # print("isWater : ", isWater)
        # print("height : ", height)

        return height


