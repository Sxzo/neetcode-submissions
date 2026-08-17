class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        def is_valid_placement(row, col, board): # O(n^2) time 
            if board[row][col] == 'Q':
                return False

            # Check horizontal attackers
            i = 0
            while i < n:
                if board[row][i] == 'Q':
                    return False
                i += 1
            # Check vertical attackers
            i = 0
            while i < n:
                if board[i][col] == 'Q':
                    return False
                i += 1
            # Check left down diagonal attackers
            tmp_row = row + 1
            tmp_col = col - 1
            while tmp_col >= 0 and tmp_row < n:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row += 1
                tmp_col -= 1
            # check right down diagonal attackers
            tmp_row = row + 1
            tmp_col = col + 1
            while tmp_col < n and tmp_row < n:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row += 1
                tmp_col += 1

            # check left up diagonal attackers
            tmp_row = row - 1
            tmp_col = col - 1
            while tmp_col >= 0 and tmp_row >= 0:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row -= 1
                tmp_col -= 1

            # check right up diagonal attackers 
            tmp_row = row - 1
            tmp_col = col + 1
            while tmp_col < n and tmp_row >= 0:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row -= 1
                tmp_col += 1
            
            return True

        board = [["."] * n for _ in range(n)]
        
        def bt(r):
            if r >= n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if is_valid_placement(r,c,board):
                    board[r][c] = "Q"
                    bt(r + 1)
                    board[r][c] = "."

        bt(0)

        return res