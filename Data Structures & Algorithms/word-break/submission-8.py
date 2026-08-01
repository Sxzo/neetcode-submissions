class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Recurrence
        # wb(len(s)) = True 
        # wb(i) = whether or not s[i:len(s)] is a valid string

        wordDict = set(wordDict)
        
        # The work on each level doubles each time it gets called
        # So our runtime complexity here is 2^n
        # T(n) = T(n - 1) + T(n - 2) + T(n - x)... + T(1)
        # O(2^n)

        memo = {}
        def wb(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return True 
            
            result = False
            for r in range(i + 1, len(s) + 1):
                word = s[i:r]
                if word in wordDict:
                    result = result or wb(r)
            memo[i] = result
            return result
        
        return wb(0)
        



        








