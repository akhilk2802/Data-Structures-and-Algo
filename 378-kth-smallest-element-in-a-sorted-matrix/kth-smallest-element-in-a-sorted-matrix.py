class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])

        print("print the heap : ", heap)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)