class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)

        # Recurrence
        # wb(i) = whether or not s[i:len(s)] can be broken up

        memo = {}

        def wb(i):
            if i in memo:
                return memo[i]
            if i > len(s):
                return False
            
            if i == len(s):
                return True
            
            result = False
            for r in range(i + 1, len(s) + 1):
                if s[i:r] in wordDict:
                    result = result or wb(r)
            memo[i] = result
            return memo[i]

        wb(0)
        return memo[0]

        # memo = [False] * (len(s) + 1)
        # memo[len(s)] = True
        
        # for i in range(len(s) - 1, -1 -1):
        #     result = False
        #     for r in range(i + 1, len(s) + 1):
        #             if s[i:r] in wordDict:
        #                 result = result or memo[r]
        
        # return memo[0]

        








