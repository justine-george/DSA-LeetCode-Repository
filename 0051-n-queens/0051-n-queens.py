class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queens puzzle. Return all possible solutions where 
        n queens can be placed on an n x n chessboard.
        
        Args:
        - n: The size of the chessboard.

        Returns:
        - List of all possible solutions.
        """
        
        col = set()
        posDiag = set() # Positive diagonal (r + c)
        negDiag = set() # Negative diagonal (r - c)
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'

                backtrack(row + 1)

                # Undo the previous placements
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = '.'

        backtrack(0)
        return res