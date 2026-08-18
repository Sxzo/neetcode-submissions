class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # def lip(i,j) = the longest increasing path to reach i,j
        # lip(i,j) = max(lip(x,y) for x in i + 1, i - 1 | for y in j + 1, j - 1)

        memo = {}
        def lip(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0

            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                res = max(res, 1 + lip(i + 1, j))
            
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + lip(i -1, j))
            
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                res = max(res, 1 + lip(i, j +1))
            
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                res= max(res, 1 + lip(i, j -1))

            memo[(i,j)] = res
            return res

        final_answer = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                final_answer = max(final_answer, 1 + lip(r, c))
        
        return final_answer
        # likely need a for loop starting from each cell
        