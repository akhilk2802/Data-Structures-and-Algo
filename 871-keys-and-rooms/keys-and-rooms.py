class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        start = 0
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(reversed([n for n in rooms[node] if n not in visited]))

        
        print(len(visited))

        return len(visited) == n
