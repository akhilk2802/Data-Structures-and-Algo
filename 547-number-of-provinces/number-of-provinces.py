class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        v = set()

        def dfs(node):
            for neighbor in range(n):
                print("neighbor :", neighbor)
                if isConnected[node][neighbor] == 1 and neighbor not in v:
                    v.add(neighbor)
                    dfs(neighbor)

        count = 0

        for city in range(n):
            if city not in v:
                count += 1
                v.add(city)
                dfs(city)

        return count

        