class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        result = []
        m1 = {}
        m2 = defaultdict(int)

        for x, y in queries:
            if x in m1:
                prev = m1[x]
                m2[prev] -= 1
                if m2[prev] == 0:
                    del m2[prev]

            m1[x] = y
            m2[y] += 1
            result.append(len(m2))

        return result