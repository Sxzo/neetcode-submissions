class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Create adj list
        # 2. Create indegree map
        # 3. Init q with all nodes where indegree == 0
        # 4. BFS, no visited set, append to q only when indegree == 0

        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        indegree = [0] * numCourses
        for course in range(numCourses):
            for incoming_course in graph[course]:
                indegree[incoming_course] += 1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        traversal = []

        while q:
            curr = q.popleft()
            traversal.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(traversal) == numCourses:
            return traversal
        else:
            return []


