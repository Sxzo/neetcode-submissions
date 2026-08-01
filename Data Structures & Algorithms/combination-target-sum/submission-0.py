class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        
        combination = []

        running_sum = 0

        def dfs(running_sum, combination, i):
            # Base case 1 where condition is met
            if running_sum == target:
                result.append(combination.copy())
                return
            
            # Base Case 2 where condition was missed
            if running_sum > target or i >= len(nums):
                return
            
            # Three options
            # 1. Add the current number and continue
            combination.append(nums[i])
            dfs(running_sum + nums[i], combination, i)
            # 3. Skip the current number
            combination.pop()
            dfs(running_sum, combination, i + 1)
        
        dfs(running_sum, combination, 0)

        return result



        