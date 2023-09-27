class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for k in range(rowIndex + 1):
            # length of row is rowIndex + 1
            row = [1] * (k + 1)

            # set start and end as 1
            row[0] = row[-1] = 1

            # update middle values
            for i in range(1, k):
                row[i] = res[-1][i - 1] + res[-1][i]
            
            # add this row to the result
            res.append(row)
        
        # return the last row
        return res[-1]
