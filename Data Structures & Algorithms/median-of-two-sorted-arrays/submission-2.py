class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Binary search on where the cut point is in the smaller of the two arrays 
        # You can compute the cut point in the larger array as a dependent of where the left cut is
        
        # Get A as the smaller array, B as the larger
        A, B = nums1, nums2
        if len(B) < len(A):
            A,B = nums2, nums1
        
        Aleft = 0 
        # This may need to be just len(A)
        Aright = len(A)

        while Aleft <= Aright:
            Acut = (Aleft + Aright) // 2
            Bcut = ((len(A) + len(B)) // 2) - Acut 

            Al = A[Acut - 1] if Acut > 0 else float('-inf')
            Ar = A[Acut] if Acut < len(A) else float('inf')
            Bl = B[Bcut - 1]  if Bcut > 0 else float('-inf')
            Br = B[Bcut] if Bcut < len(B) else float('inf')

            if Al > Br:
                Aright = Acut - 1
            elif Bl > Ar:
                Aleft = Acut + 1
            else:
                break
        
        if (len(A) + len(B)) % 2 == 0:
            return (max(Al, Bl) + min(Ar, Br)) / 2
        else:
            return min(Ar, Br)