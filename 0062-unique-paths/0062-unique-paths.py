class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dict = {(m-1, n-1): 0}
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if i == m - 1 or j == n - 1:
        #             dict[(i, j)] = 1
        #         else:
        #             dict[(i, j)] = dict[(i + 1, j)] + dict[(i, j + 1)]
        # return dict[(0, 0)]
    
    
        
        # start from bottom row
        row = [1] * n
        
        for i in range(m - 1):# go through other rows
            newRow = [1] * n # this is going to the row above bottom row
            
            # start at the second to last position, since we know the last column is all 1s, go till the beginning, in reverse order
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            
            # this new row is now row
            row = newRow
        
        # now row is the top row
        return row[0]