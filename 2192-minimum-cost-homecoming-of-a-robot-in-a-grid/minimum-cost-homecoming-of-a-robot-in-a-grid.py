class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos
        total_cost = 0

        if start_row < home_row:
            for i in range(start_row + 1, home_row + 1):
                total_cost += rowCosts[i]
        else:
            for i in range(start_row - 1, home_row - 1, -1):
                total_cost += rowCosts[i]
        
        if start_col < home_col:
            for i in range(start_col + 1, home_col + 1):
                total_cost += colCosts[i]
        else:
            for i in range(start_col - 1, home_col - 1, -1):
                total_cost += colCosts[i]
        
        return total_cost