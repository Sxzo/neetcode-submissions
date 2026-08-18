class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # def wb(i) = whether or not s[i::] can be segmented into a space separated sequence of words
        # "neetcode"
        wordDict = set(wordDict)
        memo = {}
        def wb(i):
            if memo.get(i, -1) != -1:
                return memo[i]

            if i == len(s):
                return True 
            
            final_res = False 
            for j in range(i,len(s) + 1):
                if s[i:j] in wordDict:
                    final_res = wb(j) or final_res
            
            memo[i] = final_res
            return memo[i]

        return wb(0)