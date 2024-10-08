class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        '''
        11
        121
        '''
        prev_row = [1, 1]
        for i in range(2, rowIndex + 1):
            cur_row = [1] * (i + 1)
            for j in range(1, i):
                cur_row[j] = prev_row[j-1] + prev_row[j]
            # prev_row, cur_row = cur_row, prev_row
            prev_row = cur_row
        
        return prev_row


