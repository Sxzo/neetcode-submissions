class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = set()
        def bt(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    bt(path)
                    path.pop()

        bt([])
        return res