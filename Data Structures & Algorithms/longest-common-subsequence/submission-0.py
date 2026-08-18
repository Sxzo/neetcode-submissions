class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dfs(l, r) = the LCS that can be formed between text1[l::] and text2[r::]

        memo = {}
        def dfs(l, r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l >= len(text1) or r >= len(text2):
                return 0
            
            if text1[l] == text2[r]:
                memo[(l,r)] = 1 + dfs(l + 1, r + 1)
            else:
                memo[(l,r)] = max(dfs(l + 1, r), dfs(l, r + 1))
            
            return memo[(l,r)]
            
        return dfs(0,0)
        