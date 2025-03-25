class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        '''
        lets look at what the problems is asking for ->
        sort based on x axis starting 
        sort based on y axis starting 
        '''

        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]

        def check(intervals):
            intervals.sort()

            group = 1
            current_end = intervals[0][1]

            for interval in intervals[1:]:
                start, end = interval
                if start >= current_end:
                    group += 1
                    current_end = end
                else:
                    current_end = max(current_end, end)

            return group >= 3

        return check(x_intervals) or check(y_intervals)