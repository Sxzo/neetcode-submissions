from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1,0], [0, 1], [0, -1]]
        INF = 2147483647

        # Multi-source BFS from all treasure chests, marking land as reached

        wave = 0

        q = deque()

        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) 
                    or grid[nr][nc] == -1 or (nr, nc) in visited):
                    continue 
                
                if grid[r][c] == 0:
                    grid[nr][nc] = 1
                    visited.add((nr, nc))
                    q.append((nr, nc))
                else:
                    grid[nr][nc] = grid[r][c] + 1
                    visited.add((nr, nc))
                    q.append((nr, nc))
            

