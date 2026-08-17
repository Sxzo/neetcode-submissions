class Solution:
    def numDecodings(self, s: str) -> int:
        
        # if digit == 1 then theres two options, if digit is equal to 2 and next digits are in range of 0-6, two options
        memo = {}
        def dp(i):
            if memo.get(i): 
                return memo[i]

            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = 0 

            if i + 1 < len(s) and s[i + 1] == "0":
                if s[i] == "0" or int(s[i]) > 2:
                    return 0
                else:
                    memo[i] = dp(i + 2)
            elif s[i] == "1" and i + 1 < len(s):
                memo[i] = dp(i + 2) + dp(i + 1)
            
            elif s[i] == "2" and i + 1 < len(s) and int(s[i + 1]) <= 6:
                memo[i] = dp(i + 2) + dp(i + 1)
            else:
                memo[i] = dp(i + 1)
            
            return memo[i]
        
        return dp(0)
