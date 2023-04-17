class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # T: O(log(mn)), S: O(1)
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            mid_value = matrix[mid // cols][mid % cols]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False