class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # Recurrence 
        # wb(0) = solution
        # wb(len(s)) = []
        # wb(i) = All possible sentences able to be formed from s[i:len(s)]

        def wb(i):
            # Base Case
            if i == len(s):
                return [""]
            
            solution = []
            for r in range(i, len(s) + 1):
                current_word = s[i:r]

                if current_word not in wordDict:
                    continue
                
                remaining_possibilities = wb(r)

                for remaining_possibility in remaining_possibilities:
                    if remaining_possibility == "":
                        solution.append(current_word)
                        continue
                    
                    new_sentence = current_word + " " + remaining_possibility
                    solution.append(new_sentence)
            
            return solution
                
        return wb(0)
