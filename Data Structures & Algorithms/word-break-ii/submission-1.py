class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        memo = {}
        wordDict = set(wordDict)

        def wb(i):
            if i == len(s):
                return [""]
            
            if i in memo:
                return memo[i]
            res = []
            for r in range(i + 1, len(s) + 1):
                word = s[i:r]
                if word not in wordDict:
                    continue
                
                future_possibilities = wb(r)

                for substr in future_possibilities:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
                
            memo[i] = res
            return memo[i]
        
        return wb(0)
