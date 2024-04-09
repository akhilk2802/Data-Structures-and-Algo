class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}

        for e in edges:
            if e[0] not in graph:
                graph[e[0]] = []
            if e[1] not in graph:
                graph[e[1]] = []
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        for key in graph:
            if len(graph[key]) == len(edges):
                return key
            