from collections import defaultdict
from typing import List

class Solution:
    # Add "self" parameter so it's an instance method.
    def calcDivision(self, graph, start, end):
        visited = set()
        
        def dfs(node, accumulated):
            if node == end:
                return accumulated
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor, accumulated * weight)
                    if result != -1:
                        return result
            return -1
        if start not in graph or end not in graph:
            return -1
        
        
        return dfs(start, 1.0)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_n_sol = zip(equations, values)
        graph = defaultdict(list)

        for u, v in eq_n_sol:
            x, y = u
            graph[x].append((y, v))
            graph[y].append((x, 1 / v))

        print("Graph -> ", dict(graph))
        res = []
        for query in queries:
            val = self.calcDivision(graph, query[0], query[1])
            res.append(val)
        return res