class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # consider the matrix as a m*n sorted 1d array and do binary search
#         # T: O(log(mn)), S: O(1)
#         rows, cols = len(matrix), len(matrix[0])
#         l, r = 0, rows * cols - 1
        
#         while l <= r:
#             mid = l + (r - l) // 2
#             mid_value = matrix[mid // cols][mid % cols]
#             if mid_value == target:
#                 return True
#             elif mid_value < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False
    
        
        # do one binary search to find row, then another on that row to find value
        # T: O(log(mn)), S: O(1) (because logm + logn = logmn)
        rows, cols = len(matrix), len(matrix[0])
        
        l, r = 0, rows - 1
        rowFound = False
        while l <= r:
            row = l + (r - l) // 2
            # if target is greater than the last element in the row
            if target > matrix[row][-1]:
                l = row + 1
            # if target is less than the first element in the row
            elif target < matrix[row][0]:
                r = row -1
            # if row is found out
            else:
                rowFound = True
                break
        
        if not rowFound:
            return False
        
        row = l + (r - l) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                return True
        
        return False