class Solution:
    def climbStairs(self, n: int) -> int:

        # dp(i) = the number of distinct ways to climb to i
        memo = {}
        
        def dp(i):
            if i == 0:
                return 1

            if i < 0:
                return 0
            
            if memo.get(i) == None:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)
        