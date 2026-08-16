class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def bt(index, curr_nums):
            if sum(curr_nums) == target: 
                res.append(curr_nums[:])
                return 
            if sum(curr_nums) > target or index >= len(nums):
                return
            

            
            curr_nums.append(nums[index])
            bt(index, curr_nums)
            curr_nums.pop()
            bt(index + 1, curr_nums)
        
        bt(0, [])
        return res



        