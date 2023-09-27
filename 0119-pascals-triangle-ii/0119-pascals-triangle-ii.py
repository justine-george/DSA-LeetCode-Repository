class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # T: O(rowIndex^2), S: O(rowIndex), space efficient
        prev_row = [0] * (rowIndex + 1)
        row = [0] * (rowIndex + 1)
        for k in range(rowIndex + 1):
            print(prev_row)
            # set start and end as 1
            row[0] = row[k] = 1

            # update middle values
            for i in range(1, k):
                row[i] = prev_row[i - 1] + prev_row[i]

            # row is the prev_row for next iteration
            prev_row = row[:]
        
        # return prev_row
        return prev_row
# p
# c    [1, 0, 0, 0]
#     [1, 1, 0, 0]
#     [1, 2, 1, 0]
#     [1, 3, 3, 1]

        # # recursive solution, but takes O(n^2) space
        # row = [1] * (rowIndex + 1)
        # if rowIndex == 0:
        #     return row
        
        # prev_row = self.getRow(rowIndex - 1)
        # for i in range(1, len(row) - 1):
        #     row[i] = prev_row[i - 1] + prev_row[i]
        
        # return row