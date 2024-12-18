import heapq

class MedianFinder:

    def __init__(self):
        # Max-Heap (stores smaller half, negate values)
        self.small = []  
        # Min-Heap (stores larger half)
        self.large = []  

    def addNum(self, num: int) -> None:
        # Add to max-heap first
        heapq.heappush(self.small, -num)
        
        # Ensure every number in `small` is <= every number in `large`
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Balance the heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])  # Max-Heap top element
        else:
            # Average of tops from both heaps
            return (-self.small[0] + self.large[0]) / 2.0