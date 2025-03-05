class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        
        # adj = defaultdict(list)
        # for u, v in prerequisites:
        #     adj[u].append(v)
        # print("ADj :", adj)

        # visited = [0] * n

        # def dfs(node):
        #     if visited[node] == 1:
        #         return False
        #     if visited[node] == 2:
        #         return True

        #     visited[node] = 1

        #     for neighbor in adj[node]:
        #         if not dfs(neighbor):
        #             return False

        #     visited[node] = 2
        #     return True

        # for course in range(n):
        #     if visited[course] == 0:
        #         if not dfs(course):
        #             return False

        # return True

        adj = defaultdict(list)
        indegree = [0] * n
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        # print("ADJ : ", adj)
        # print("IN : ", indegree)

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []

        while q:
            node = q.popleft()

            topo.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # print("TOPO : ", topo)

        return len(topo) == n