class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # dfs(r, c) = the number of unique paths that can be taken to reach r,c from 0,0

        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r < 0 or c < 0 or r == m or c == n:
                return 0

            if r == 0 and c == 0:
                return 1
            memo[(r,c)] = dfs(r - 1, c) + dfs(r, c - 1)
            return memo[(r,c)]
        
        return dfs(m - 1,n - 1)