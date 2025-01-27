class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjlist = defaultdict(list)
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)

        indegree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]

        # print("Prereq_sets : ", prereq_sets)

        for pre, courses in adjlist.items():
            for course in courses:
                indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            for neighbor in adjlist[current]:
                prereq_sets[neighbor].update(prereq_sets[current])
                prereq_sets[neighbor].add(current)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        result = []

        print("sets : ", prereq_sets)
        for u, v in queries:
            result.append(v in prereq_sets[u])
        
        return result
        