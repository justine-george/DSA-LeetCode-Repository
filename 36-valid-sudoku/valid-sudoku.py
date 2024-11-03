class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = {i: set() for i in range(9)}
        cset = {i: set() for i in range(9)}
        gset = {(i, j): set() for i in range(3) for j in range(3)}
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur != '.':
                    if cur in rset[r] or cur in cset[c] or cur in gset[(r // 3, c // 3)]:
                       return False
                    rset[r].add(cur)
                    cset[c].add(cur)
                    gset[(r // 3, c // 3)].add(cur)
        return True