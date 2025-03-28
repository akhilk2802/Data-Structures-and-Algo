from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        '''
        couldn't solve the first time, had to look at editorial lol
        revise this problem later -> really good problem
        '''

        row_count, col_count = len(grid), len(grid[0])
        result = [0] * len(queries)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        min_heap = PriorityQueue()
        visited = [[False] * col_count for _ in range(row_count)]
        total_points = 0
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = True

        for query_value, query_index in sorted_queries:
            while not min_heap.empty() and min_heap.queue[0][0] < query_value:
                cellValue, current_row, current_col = min_heap.get()

                total_points += 1

                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = (
                        current_row + row_offset,
                        current_col + col_offset,
                    )

                    if (
                        new_row >= 0
                        and new_col >= 0
                        and new_row < row_count
                        and new_col < col_count
                        and not visited[new_row][new_col]
                    ):
                        min_heap.put((grid[new_row][new_col], new_row, new_col))
                        visited[new_row][new_col] = True
            result[query_index] = total_points

        return result