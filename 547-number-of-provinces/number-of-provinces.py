class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        adj_list = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)

        # print("Adjacency list : ", adj_list)
        visited = set()
        count = 0 

        def dfs(node):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        print("count : ", count)
        return count


