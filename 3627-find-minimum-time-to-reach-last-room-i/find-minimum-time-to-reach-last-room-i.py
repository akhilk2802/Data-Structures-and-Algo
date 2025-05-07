class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        numRows = len(moveTime)
        numCols = len(moveTime[0])

        minHeap = [(0, 0, 0)]
        arrivalTime = [[float('inf')] * numCols for _ in range(numRows)]
        arrivalTime[0][0] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            currentTime, x, y = heapq.heappop(minHeap)

            if (x, y) == (numRows - 1, numCols - 1):
                return currentTime

            for dx, dy in directions:
                newX, newY = x + dx, y + dy

                if 0 <= newX < numRows and 0 <= newY < numCols:
                    waitTime = max(moveTime[newX][newY] - currentTime, 0)
                    newArrivalTime = currentTime + 1 + waitTime

                    if newArrivalTime < arrivalTime[newX][newY]:
                        arrivalTime[newX][newY] = newArrivalTime
                        heapq.heappush(minHeap, (newArrivalTime, newX, newY))

        return -1