class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        '''
        brute force approach ->
        write a function for this -> check if subgraph is complete
        check number of components
        '''

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print("graph : ", graph)

        visited = set()
        count = 0

        def dfs(node, component):
            component.add(node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    count += 1
        
        # print("count : ", count)
        return count