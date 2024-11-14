class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posdiags, negdiags = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]
        
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or r + c in posdiags or r - c in negdiags:
                    continue
                cols.add(c)
                posdiags.add(r + c)
                negdiags.add(r - c)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.remove(c)
                posdiags.remove(r + c)
                negdiags.remove(r - c)
                board[r][c] = '.'

        dfs(0)
        return res