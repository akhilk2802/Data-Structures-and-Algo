class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        m = defaultdict(list)

        for id, score in items:
            heapq.heappush(m[id], score)
            if len(m[id]) > 5:
                heapq.heappop(m[id])

        result = []
        for s_id in sorted(m.keys()):
            avg_score = sum(m[s_id]) // 5
            result.append([s_id, avg_score])

        return result

        # print("m : ", m)

        