class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]: continue

            target = 0 - nums[i]

            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                
                if curr_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    prev_left = nums[left]
                    while left < right and prev_left == nums[left]:
                        left += 1
                elif curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
            
        return res 
        
# [-1, -1, 0, 1, 2]
        