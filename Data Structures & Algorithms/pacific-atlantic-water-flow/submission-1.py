class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        # BFS
        # Two multi-source traversals
        # One from the pacific bordering cells
        # Store what elements are reachable from the pacific
        # One from the atlantic bordering cells 
        # Store what elements are reachable from the atlantic 
        # Return intersection of both sets 



        ROWS = len(heights)
        COLS = len(heights[0])
        
        def takeStep(row, col, prev_height, visited, q):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row,col) in visited or heights[row][col] < prev_height:
                return
            
            q.append([row, col])
            visited.add((row, col))


        def bfs(ocean):
            q = deque([])

            # Initialize sources 
            for row, col in ocean:
                q.append([row, col])
            
            while q:
                row, col = q.popleft()
                curr_height = heights[row][col]

                takeStep(row + 1, col, curr_height, ocean, q)
                takeStep(row - 1, col, curr_height, ocean, q)
                takeStep(row, col + 1, curr_height, ocean, q)
                takeStep(row, col - 1, curr_height, ocean, q)
            

        
        atlantic_reachable = set()
        pacific_reachable = set()

        # Initialize border elements
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    atlantic_reachable.add((row, col))
                
                if row == ROWS - 1 or col == COLS - 1:
                    pacific_reachable.add((row, col))
        
        bfs(atlantic_reachable)
        bfs(pacific_reachable)
        
        tuple_answer = atlantic_reachable.intersection(pacific_reachable)

        return [list(c) for c in tuple_answer]

        