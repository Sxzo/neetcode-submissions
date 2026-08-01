class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Split the array into two sorted partitions, left and right
        # 2. If the size is even, take the max between the two leftmost and the min between the two rightmost
        # 2.5 If the size is odd, take the max between the left, and the min between the right then sum and / 2
        
        # [1,2,3|4,5,6]
        # [1,5|6,7,8]
        # total elements = 11
        

        # First get the smaller array. A == smaller array
        A, B = nums1, nums2
        if len(A) > len(B):
            A = nums2
            B = nums1
        
        Aleft = 0
        Aright = len(A)
        # While the partition remains invalid: 
        while Aleft <= Aright:
            Acut = (Aleft + Aright) // 2
            Bcut = (len(A) + len(B)) // 2 - Acut
            
            Al = A[Acut - 1] if Acut > 0 else float('-inf')
            Ar = A[Acut] if Acut < len(A) else float('inf')
            Bl = B[Bcut - 1] if Bcut > 0 else float('-inf')
            Br = B[Bcut] if Bcut < len(B) else float('inf')


            if Al > Br:
                Aright = Acut - 1
            elif Ar < Bl:
                Aleft = Acut + 1
            else:
                break
        
        if (len(A) + len(B)) % 2 == 0:
            median = (max(Al, Bl) + min(Ar, Br)) / 2 
        else:
            median = min(Ar, Br) 
        
        return median
