class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            setRow = set()
            setCol = set()
            for j in range(len(board[0])):
                # check all rows
                if board[i][j] != ".":
                    if board[i][j] in setRow:
                        return False
                    setRow.add(board[i][j])
                # check all columns
                if board[j][i] != ".":
                    if board[j][i] in setCol:
                        return False
                    setCol.add(board[j][i])
        
        # check all 3x3s
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                set3x3 = set()
                for i in range(m, m + 3):
                    for j in range(n, n + 3):
                        if board[i][j] != ".":
                            if board[i][j] in set3x3:
                                return False
                            set3x3.add(board[i][j])

        return True