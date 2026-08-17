class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(curr_sum):
            if memo.get(curr_sum):
                return memo[curr_sum]
            if curr_sum > amount:
                return float('inf')
            
            if curr_sum == amount:
                return 0
            
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(curr_sum + coin))
            
            memo[curr_sum] = res
            return res
        
        res = dfs(0)
        if res == float('inf'):
            return -1
        else:
            return res
            


        