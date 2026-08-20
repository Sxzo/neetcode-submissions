class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0,1]]
        # Traversal is only possible to neighbors with height <= curr_height 
        # for each cell, two BFS traversals - one to reach the pacific, one for the atlantic
        # atlantic -> row = len(heights) - 1 or col =len(heights[0]) - 1
        # pacific -> col = 0 or row = 0

        def bfs(i,j):
            
            atl_pac = [False, False]

            q = deque([(i,j)])
            visited = set([(i,j)])

            while q:
                r, c = q.popleft()
                
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atl_pac[0] = True
                
                if r == 0 or c == 0:
                    atl_pac[1] = True 

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or nr >= len(heights) or nc >= len(heights[0]) 
                        or (nr, nc) in visited or heights[nr][nc] > heights[r][c]):
                        continue 
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
            
            return atl_pac
        
        res = []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                atl, pac = bfs(r, c)
                if atl and pac:
                    res.append([r,c])
        
        return res



            


        