class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        # Initialize graph as adj list 
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        

        inDegree = defaultdict(int)

        # Create in degree, which equals node -> mapping of incoming edges
        for neighbors in graph.values():
            for neighbor in neighbors:
                inDegree[neighbor] += 1
        print(inDegree)
        q = deque()

        # initialize all sources in the queue 
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        traversal = []

        while q:
            curr = q.popleft()
            traversal.append(curr)
            for neighbor in graph[curr]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)
        
        print(traversal)
        return len(traversal) == numCourses



        
        


