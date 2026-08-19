class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # def dp(i,j) = min edit distance of word1[i::] and word2[j::]
        # dp(len(word1), len(word2)) = 0

        memo = {}

        def dp(i,j):
            if (i,j) in memo:
                return memo[i,j]
            
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i + 1, j + 1)
            else:
                memo[(i,j)] = min(1 + dp(i + 1, j), 1 + dp(i, j +1), 1 + dp(i + 1, j + 1))
            
            return memo[(i,j)]
        
        return dp(0,0)
            

        