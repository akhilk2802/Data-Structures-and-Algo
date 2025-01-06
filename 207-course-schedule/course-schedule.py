class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        visited = [0] * n

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2
            return True

        for course in range(n):
            if visited[course] == 0:
                if not dfs(course):
                    return False

        return True
