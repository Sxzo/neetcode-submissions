class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Idea:
        # Sort the array and store a prev number to know when a choice can be made to include or not
        
        candidates.sort()
        
        results_set = set()
        curr_combo = []
        running_sum = 0
        
        def dfs(running_sum, curr_combo, i):
            if running_sum == target:
                results_set.add(tuple(curr_combo))
                return
            if running_sum > target or i >= len(candidates):
                return
            # Two cases
            # Condition: if prev == cur, only skip
            # otherwise two choices: 
            # 1. Add the current number
            # 2. Skip the current number

            curr_combo.append(candidates[i])
            dfs(running_sum + candidates[i], curr_combo,  i + 1)
            curr_combo.pop()
            dfs(running_sum, curr_combo, i + 1)   
 
        dfs(0, [], 0)

        results = [list(t) for t in results_set]

        return results
            


#             if prev == -1:
               # curr_combo.append(candidates[i])
                #dfs(running_sum + candidates[i], curr_combo, candidates[i], i + 1)
            #elif prev == candidates[i]:
                #dfs(running_sum, curr_combo, candidates[i], i + 1)
            # else: