class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        # dfs(i, j) = the LIS starting from i where i > j
        memo = {}
        def dfs(i, j):
            if memo.get((i, j)):
                return memo[(i,j)]
            
            if i == len(nums):
                return 0
            

            if j == float('-inf') or nums[i] > nums[j]:
                memo[(i,j)] = max(1 + dfs(i + 1, i), dfs(i + 1, j))
            else:
                memo[(i,j)] = dfs(i + 1, j)
            
            return memo[(i,j)]

        return dfs(0, float('-inf'))
            
        
        