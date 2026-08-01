class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [-1, 0, 8, 12, 13]

        # [12, 13, -1, 0, 8]

        # [8, 12, 13, -1, 0]

        # [0, 8, 12, 13, -1]

        # if right > mid, the cut is == to or to the left 
        # if right < mid, the cut is to the right 

        left = 0
        right = len(nums) - 1
        min_num = 999
        while left <= right:
            print("l:", left, "r:", right)
            mid = (left + right) // 2
            print(mid)
            min_num = min(min_num, nums[mid])

            if nums[right] >= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return min_num
