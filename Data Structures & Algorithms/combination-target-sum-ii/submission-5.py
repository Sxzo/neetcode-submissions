class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        # [1,2,2,2,4,5,6,9]
        
        def bt(i, path, s):
            if s == target:
                res.append(path[:])
                return
            
            if i >= len(candidates) or s > target:
                return
            
            # Get j to be the first index where nums[j] != nums[i]
            j = i
            while j < len(candidates) - 1 and candidates[j] == candidates[j + 1]:
                j += 1
            j += 1


            for z in range(i,j):
                path.append(candidates[i])
                s+= candidates[i]
                bt(j, path, s)
            
            for _ in range(i, j):
                path.pop()
                s -= candidates[i]
            
            bt(j, path, s)
            
        bt(0, [], 0)

        return res
