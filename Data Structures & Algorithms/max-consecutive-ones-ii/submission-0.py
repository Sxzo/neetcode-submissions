class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        def dfs(i, flipped):
            if i >= len(nums) or (nums[i] == 0 and flipped == True):
                return 0
            
            if nums[i] == 1:
                return 1 + dfs(i + 1, flipped)
            else:
                return 1 + dfs(i + 1, True)
        
        max_val = 0
        for i in range(len(nums)):
            max_val = max(max_val, dfs(i, False))

        return max_val