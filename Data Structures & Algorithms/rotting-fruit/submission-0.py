from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_in_bounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        q = deque()
        fresh_fruit = 0

        # Get and insert sources
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append(((r, c), 0))
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        max_time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh_fruit > 0:
            (r, c), depth = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_in_bounds(nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_fruit -= 1
                    q.append(((nr, nc), depth + 1))
                    max_time = max(max_time, depth + 1)

        return -1 if fresh_fruit != 0 else max_time