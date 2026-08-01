class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Go through each possible starting element of the grid
        # If its -1, continue, if its 0, continue
        # if its a land cell, remember its index
        # Then perform BFS, keeping track of distance, 
        # and short circuit whenever a treasure chest is found and set the land cell index = to the distance value            

        # O(M)
        def bfs(row, col):
            q = deque([(row,col,0)])
            visited = set([(row,col)])

            # While our queue is not empty
            while q:
                row, col, distance = q.popleft() 

                if grid[row][col] == 0:
                    return distance

                if col - 1 >= 0 and grid[row][col - 1] >= 0:
                    if (row, col - 1) not in visited:
                        q.append((row, col - 1, distance + 1))
                        visited.add((row, col - 1))
                
                if col < len(grid[0]) - 1 and grid[row][col + 1] >= 0:
                    if (row, col + 1) not in visited:
                        q.append((row, col + 1, distance + 1))
                        visited.add((row, col - 1))
                
                if row - 1 >= 0 and grid[row - 1][col] >= 0:
                    if (row - 1, col) not in visited:
                        q.append((row - 1, col, distance + 1))
                        visited.add((row - 1, col))
                
                if row < len(grid) - 1 and grid[row + 1][col] >= 0:
                    if (row + 1, col) not in visited:
                        q.append((row + 1, col, distance + 1))
                        visited.add((row + 1, col))
            
            return 2147483647

        # O(m * n)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell_val = grid[row][col]

                # If the current cell is NOT a land cell
                if cell_val == -1 or cell_val == 0: 
                    continue 
                
                grid[row][col] = bfs(row, col)
    
        return