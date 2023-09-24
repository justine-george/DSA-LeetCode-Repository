class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # try every single position on the current row
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # add to the sets and the board
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                
                # now check next row with this updated board
                backtrack(r + 1)
                
                # undo the changes
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        
        # start from row 0
        backtrack(0)
        
        return res