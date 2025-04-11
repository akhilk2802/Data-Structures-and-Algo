from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        visited = set()
        count = 0
        components = []

        def dfs(node, comp):
            # if node not in visited:
            visited.add(node)
            comp.add(node)
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, comp)
            

        for i in range(n):
            if i not in visited:
                # print("I -> ", i)
                comp = set()
                dfs(i, comp)
                count += 1
                components.append(comp)
                
        # print("Count : ", count)
        print("components: ", components)
        return count