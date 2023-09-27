class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        # go through every row, starting from second row
        for i in range(1, query_row + 1):
            cur = [0] * (i + 1) # size 2 for the second row
            
            for j in range(i):
                extra = prev[j] - 1 if prev[j] > 1 else 0

                cur[j] += (0.5 * extra)
                cur[j + 1] += (0.5 * extra)
            
            prev = cur
        
        return min(1, prev[query_glass])