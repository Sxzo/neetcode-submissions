from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1,0], [0, -1], [0, 1]]
        
        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = 0
            area = 0

            while q:
                row, col = q.popleft()
                area += 1 

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0])
                        and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            
            return area





        largest_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    largest_area = max(largest_area, bfs(r,c))
        
        return largest_area