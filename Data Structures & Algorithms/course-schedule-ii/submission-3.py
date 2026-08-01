class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses

        # Initialize the graph adjacency list
        graph = {i:[] for i in range(numCourses)}
        for course, prq in prerequisites:
            graph[prq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order_result = []

        while q:
            curr_node = q.popleft()
            order_result.append(curr_node)

            for neighbor in graph[curr_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(order_result) != numCourses:
            return []
        
        return order_result
        


        