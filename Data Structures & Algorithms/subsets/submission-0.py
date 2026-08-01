class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def dfs(curr_subset, i):
            if i == len(nums):
                result.append(curr_subset.copy())
                return
            
            subset.append(nums[i])
            dfs(subset, i+1)
            subset.pop()
            dfs(subset, i+1)
        
        dfs(subset, 0)

        return result
        