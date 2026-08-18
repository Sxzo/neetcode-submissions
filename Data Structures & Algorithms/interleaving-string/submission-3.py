class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # inter(i, j) = whether s1[i::] and s2[j::] can be intervleaved to form s3[i + j::]

        memo = {}
        def inter(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s1) and j == len(s2):
                return True
            if i == len(s1):
                return s2[j::] == s3[i + j::]
            if j == len(s2):
                return s1[i::] == s3[i + j::]
            
            if s1[i] != s3[i + j] and s2[j] != s3[i + j]:
                return False
            elif s1[i] == s3[i + j] and s2[i] == s3[i + j]:
                memo[(i,j)] = inter(i + 1, j) or inter(i, j + 1)
            elif s1[i] == s3[i + j]:
                memo[(i,j)] = inter(i + 1, j)
            else:
                memo[(i,j)] = inter(i, j + 1)
            
            return memo[(i,j)]
        
        return inter(0,0)

            
