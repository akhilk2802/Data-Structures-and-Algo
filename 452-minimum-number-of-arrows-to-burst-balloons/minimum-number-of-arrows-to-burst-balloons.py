class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        print("points -> ", points)

        arrows = 1
        current_arrow_position = points[0][1]

        for start, end in points[1:]:
            if start > current_arrow_position:
                arrows += 1
                current_arrow_position = end

        return arrows