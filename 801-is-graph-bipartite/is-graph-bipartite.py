class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        numOfNodes = len(graph)
        color = [-1] * numOfNodes

        for start in range(numOfNodes):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0

                while queue:
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True