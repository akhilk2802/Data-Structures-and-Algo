class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[0])
        min_heap = []

        for interval in intervals:
            start, end = interval

            if min_heap and min_heap[0] <= start:
                heappop(min_heap)

            heappush(min_heap, end)

        return len(min_heap)