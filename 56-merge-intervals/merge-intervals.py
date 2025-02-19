class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print("Intervals : ", intervals)

        result = []
        for i in intervals:
            if not result or result[-1][1] < i[0]:
                result.append(i)
            if result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])

        print("result : ", result)
        return result