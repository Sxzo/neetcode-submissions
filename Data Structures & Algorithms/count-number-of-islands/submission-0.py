from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Run BFS on each non-zero node, changing them to 0 as visited 

        def bfs(i,j):    
            q = deque()

            q.append((i,j))

            while q:
                curr_node_i, curr_node_j = q.pop()
                grid[curr_node_i][curr_node_j] = "0" # mark visited 

                # left 
                if curr_node_j > 0 and grid[curr_node_i][curr_node_j - 1] == "1":
                    q.append((curr_node_i, curr_node_j - 1))
                
                # right
                if curr_node_j < len(grid[0]) - 1 and grid[curr_node_i][curr_node_j + 1] == "1":
                    q.append((curr_node_i, curr_node_j + 1))
                
                # up
                if curr_node_i > 0 and grid[curr_node_i - 1][curr_node_j] == "1":
                    q.append((curr_node_i - 1, curr_node_j))

                # down
                if curr_node_i < len(grid) - 1 and grid[curr_node_i + 1][curr_node_j] == "1":
                    q.append((curr_node_i + 1, curr_node_j))




        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        
        return res
        