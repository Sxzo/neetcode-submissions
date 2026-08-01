class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_matrix_val(idx):
            row_index = idx // len(matrix[0])
            col_index = idx % len(matrix[0])
            return matrix[row_index][col_index]
        
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if get_matrix_val(mid) == target:
                return True
            elif get_matrix_val(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False