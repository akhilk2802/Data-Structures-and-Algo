class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        bob_times = {}
        def dfs(src, prev, time):
            if src == 0:
                bob_times[src] = time
                return True

            for nei in adj[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        q = deque([(0, 0, -1, amount[0])])
        res = float("-inf")

        while q:
            node, time, parent, profit = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2

                q.append((nei, nei_time, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)

        return res