class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def count_less_equal(val: int) -> int:
            """Returns the number of elements in the matrix less than or equal to val."""
            total = 0
            for row in grid:
                # Find the position where val could be inserted in the sorted row.
                l, r = 0, len(row) - 1
                while l <= r:
                    m = (l + r) // 2
                    if row[m] <= val:
                        l = m + 1
                    else:
                        r = m - 1
                total += l  # Add the count of numbers less than or equal to val in this row.
            return total
        
        m, n = len(grid), len(grid[0])
        median_position = m * n // 2 + 1
        
        # Binary search for the median value.
        l, r = 1, 10 ** 6
        while l <= r:
            mid = (l + r) // 2
            if count_less_equal(mid) < median_position:
                l = mid + 1
            else:
                r = mid - 1
                
        return l