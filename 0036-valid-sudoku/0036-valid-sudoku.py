class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = {i: [] for i in range(9)}
        cset = {i: [] for i in range(9)}
        gset = {(i, j): [] for i in range(3) for j in range(3)}
        
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur != '.':
                    if cur in rset[r]:
                        return False
                    rset[r].append(cur)

                    if cur in cset[c]:
                        return False
                    cset[c].append(cur)

                    if cur in gset[(floor(r / 3), floor(c / 3))]:
                        return False
                    gset[(floor(r / 3), floor(c / 3))].append(board[r][c])
        
        return True