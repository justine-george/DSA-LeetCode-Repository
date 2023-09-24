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
        pos_diag = set() # Positive diagonal (r + c)
        neg_diag = set() # Negative diagonal (r - c)
        res = []
        board = [["."] * n for _ in range(n)]

        self.backtrack(0, n, board, col, pos_diag, neg_diag, res)
        return res

    def backtrack(self, row: int, n: int, board: List[List[str]], col: Set[int],
                  pos_diag: Set[int], neg_diag: Set[int], res: List[List[str]]) -> None:
        if row == n:
            res.append(["".join(r) for r in board])
            return

        for c in range(n):
            if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(row + c)
            neg_diag.add(row - c)
            board[row][c] = 'Q'

            self.backtrack(row + 1, n, board, col, pos_diag, neg_diag, res)

            # Undo the previous placements
            col.remove(c)
            pos_diag.remove(row + c)
            neg_diag.remove(row - c)
            board[row][c] = '.'