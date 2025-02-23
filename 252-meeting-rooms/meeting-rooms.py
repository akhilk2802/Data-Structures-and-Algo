class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        n = len(intervals)
        if n == 0: return True
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        print("intervals : ", sorted_intervals)
        prev = sorted_intervals[0][1]
        count = 1

        for i in range(1, n):
            if sorted_intervals[i][0] >= prev:
                count += 1
                prev = sorted_intervals[i][1]
            else:
                return False

        return n == count

        