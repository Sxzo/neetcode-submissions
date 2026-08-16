class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def bt(index, subset):
            if len(subset) == len(nums) or index >= len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[index])
            bt(index + 1, subset)
            subset.pop()
            bt(index + 1, subset)


        bt(0, [])
        return result