class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # more efficient, iteration in 9^2
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        tinysquares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (board[r][c] in rows[r] or 
                        board[r][c] in cols[c] or
                        board[r][c] in tinysquares[(r // 3, c // 3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    tinysquares[(r // 3, c // 3)].add(board[r][c])
                    
        return True