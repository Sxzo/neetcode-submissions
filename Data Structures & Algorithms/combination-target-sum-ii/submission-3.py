class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        def bt(index, curr_nums):
            if sum(curr_nums) > target:
                return

            if sum(curr_nums) == target:
                res.append(curr_nums[:])
                return
            

            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue 
                
                curr_nums.append(candidates[i])
                bt(i + 1, curr_nums)
                curr_nums.pop()            

        bt(0, [])

        return res
        