from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            area = 0

            q = deque()

            q.append((i,j))

            grid[i][j] = 0

            while q:
                r,c = q.popleft()
                area += 1
                
                # left 
                if c > 0 and grid[r][c - 1] == 1:
                    q.append((r, c - 1))
                    grid[r][c - 1] = 0
                
                # right
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    q.append((r, c + 1))
                    grid[r][c + 1] = 0
                
                # up
                if r > 0 and grid[r - 1][c] == 1:
                    q.append((r - 1, c))
                    grid[r - 1][c] = 0

                # down
                if r < len(grid) - 1 and grid[r + 1][c] == 1:
                    q.append((r + 1, c))
                    grid[r + 1][c] = 0

            return area

        largest_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    largest_area = max(largest_area, bfs(r,c))
        
        return largest_area