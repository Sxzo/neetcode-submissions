class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        answer = []

        def bt(row, col, curr_word):
            if curr_word == word:
                answer.append(True)
                return 

            # up, down, left, right
            if row > 0 and board[row - 1][col] == word[len(curr_word)]:
                tmp = board[row][col] 
                board[row][col] = "1"
                bt(row - 1, col, curr_word + board[row - 1][col])
                board[row][col] = tmp
            if row < len(board) - 1 and board[row + 1][col] == word[len(curr_word)]:
                tmp = board[row][col] 
                board[row][col] = "1"
                bt(row + 1, col, curr_word + board[row + 1][col])
                board[row][col] = tmp
            if col < len(board[0]) - 1 and board[row][col + 1] == word[len(curr_word)]:
                tmp = board[row][col] 
                board[row][col] = "1"
                bt(row, col + 1, curr_word + board[row][col + 1])
                board[row][col] = tmp
            if col > 0 and board[row][col - 1] == word[len(curr_word)]:
                tmp = board[row][col] 
                board[row][col] = "1"
                bt(row, col - 1, curr_word + board[row][col - 1])
                board[row][col] = tmp
            


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    bt(r, c, str(word[0]))

        if len(answer) > 0: 
            return True 
        else: 
            return False
        