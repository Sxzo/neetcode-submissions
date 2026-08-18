class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 or len(nums) <= 1:
            return False 
        
        # dp(i) = true / false depending if there's a partition starting at i that can add to target
        # target == 0.5 * sum(nums)

        memo = {}
        def dp(i, target):
            if (i, target) in memo:
                return memo[(i,target)]
            if i >= len(nums):
                return False 
            
            if target == 0:
                return True 
            
            res = False

            for j in range(i, len(nums)):
                res = dp(j + 1, target - nums[j]) or res 
            memo[(i, target)] = res
            return res

        return dp(0, sum(nums) / 2)