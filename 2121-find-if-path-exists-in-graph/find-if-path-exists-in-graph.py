class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ad = defaultdict(list) #adjacency matrix
        for i in edges:
            ad[i[0]].append(i[1])
            ad[i[1]].append(i[0])
        q = []
        bfs = [0]*(n)
        bfs[source] = 1
        q.append(source)
        while q:
            bfs.append(q[0])
            x = q.pop(0)
            if x==destination:
                return 1
            for i in ad[x]:
                if bfs[i]==0:
                    q.append(i)
                    bfs[i] = 1
        return 0