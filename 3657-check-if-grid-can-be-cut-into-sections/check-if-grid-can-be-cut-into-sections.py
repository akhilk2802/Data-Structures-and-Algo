class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        '''
        lets look at what the problems is asking for ->
        sort based on x axis starting 
        sort based on y axis starting 
        '''

        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]

        # print("x_intervals : ", x_intervals)
        # print("y_intervals : ", y_intervals)

        def check(intervals):
            intervals.sort()
            print("sorted -> ", sorted(intervals))

            section = 0
            max_end = intervals[0][1]
            
            for start, end in intervals:
                if max_end <= start:
                    section += 1
                max_end = max(max_end, end)

            return section >= 2

        return check(x_intervals) or check(y_intervals)