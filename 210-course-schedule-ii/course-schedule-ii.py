class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjlist = defaultdict(list)
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)

        print("adj list : ", adjlist)

        indegree = [0] * numCourses
        for pre, courses in adjlist.items():
            for course in courses:
                indegree[course] += 1

        result = []
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in adjlist[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != numCourses:
            return []

        return result