class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # Run BFS / DFS on all "O" nodes that are on a border, replace these with a "Y"
        # Run BFS on all other "O" nodes that remain, replacing them with X's as you go
        # Done 

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c, char):
            
            q = deque([(r,c)])
            board[r][c] = char

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0])
                        or board[nr][nc] in [char, "X"]): # Worth double checking this last cond
                        continue 
                    
                    q.append((nr, nc))
                    board[nr][nc] = char
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if ((r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0]) - 1)
                    and board[r][c] == "O"):
                    bfs(r, c, "Y")
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    bfs(r, c, "X")
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "Y":
                    board[r][c] = "O"




            