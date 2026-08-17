class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # 1, 1, 2

        def bt(i, path):
            if i >= len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            bt(i + 1, path)
            path.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            bt(i + 1, path)
        
        bt(0, [])

        return res


        