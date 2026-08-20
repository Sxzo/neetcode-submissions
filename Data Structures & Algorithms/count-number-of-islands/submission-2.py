from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[-1, 0], [1, 0], [0,-1], [0,1]]

        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = "0"
            
            while q:
                r_, c_ = q.popleft()

                for dr, dc in directions:
                    nr, nc = r_ + dr, c_ + dc
                    if (nr >= 0 and nc >= 0 
                        and nr < len(grid) and nc < len(grid[0]) 
                        and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"


        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        
        return res