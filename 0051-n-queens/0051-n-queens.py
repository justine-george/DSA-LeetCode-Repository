class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        cols = set()
        pos_diags = set()
        neg_diags = set()

        def backtrack(r):
            if r == n:
                print(r)
                res.append(["".join(row) for row in board])

            # go through all columns of this row
            for c in range(n):
                if c in cols or r + c in pos_diags or r - c in neg_diags:
                    continue

                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res