from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # multi source BFS from all rotten fruit, replace fresh fruit with time unti infected
        # then go through all elements and return the max infection time
        # if theres any fresh return -1 

        # -1 = empty cell
        # INF = fresh fruit 
        # 0 = rotten fruit 

        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                curr_val = grid[r][c]

                if curr_val == 0:
                    grid[r][c] = -1
                elif curr_val == 1:
                    grid[r][c] = float('inf')
                else:
                    grid[r][c] = 0
        print(grid)
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
                    or (nr,nc) in visited or grid[nr][nc] == -1):
                    continue 
                
                q.append((nr,nc))
                visited.add((nr,nc))
                grid[nr][nc] = 1 + grid[r][c]
        
        max_time = 0 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_time = max(grid[r][c] ,max_time)
        
        if max_time == float('inf'):
            return -1
        else:
            return max_time

