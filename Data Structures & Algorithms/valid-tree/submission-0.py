class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # whether the size of the BFS traversal = n
        # whether any node runs into a node its already seen, other than its parent

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)

        q = deque([0])
        visited = set([0])
        traversal = []

        while q:
            curr = q.popleft()
            traversal.append(curr)
            visited_neighbors = 0

            for neighbor in graph[curr]:
                if neighbor in visited:
                    visited_neighbors += 1
                    continue 
                q.append(neighbor)
                visited.add(neighbor)
            
            if visited_neighbors > 1:
                return False
        
        if len(traversal) != n:
            return False
        
        return True 




