class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]
        # [7,0,1,2]
        # [5,1,3]

        # if right > mid, the sequence is on the right
        # else, the sequence is on the left 
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]: # If theres an increasing sequence from mid -> right
                if target > nums[mid] and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1 
 
        return -1
        