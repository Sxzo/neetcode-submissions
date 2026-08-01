class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        # You can check if an element exists in O(1) time 

        nums_set = set(nums)

        starting_numbers = []

        for n in nums_set:
            if n - 1 not in nums_set and n + 1 in nums_set:
                starting_numbers.append(n)
        
        longest_seq = 1
        
        for num in starting_numbers:
            curr_seq = 1
            while num + 1 in nums_set:
                curr_seq += 1
                num = num + 1
            longest_seq = max(curr_seq, longest_seq)
        
        return longest_seq 
            
            

        