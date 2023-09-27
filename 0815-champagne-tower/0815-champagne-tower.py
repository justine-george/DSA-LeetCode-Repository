class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the flow
        prev_row = [poured]

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            
            # for every parent item
            for j in range(row):
                extra = prev_row[j] - 1
                if extra > 0:
                    cur_row[j] += (0.5 * extra)
                    cur_row[j + 1] += (0.5 * extra)

            prev_row = cur_row
        
        return min(1, prev_row[query_glass])