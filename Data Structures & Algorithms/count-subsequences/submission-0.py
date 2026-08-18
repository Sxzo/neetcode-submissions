class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        # def dp(i,j) = the number of distinct subsequences of s[i::] that are equal to t[j::]
        
        memo = {}
        def nd(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0
            

            if s[i] == t[j]:
                memo[(i,j)] = nd(i + 1, j + 1) + nd(i + 1, j)
            else:
                memo[(i,j)] = nd(i + 1, j)
            
            return memo[(i,j)]
        
        return nd(0, 0)

        