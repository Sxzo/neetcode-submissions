class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starting_nums = []

        lcs = 0

        for n in nums:
            if n - 1 not in nums:
                starting_num = n
                curr_lcs = 1
                while starting_num + 1 in nums:
                    starting_num += 1
                    curr_lcs += 1
                lcs=max(curr_lcs, lcs)
        
        return lcs 
        

        