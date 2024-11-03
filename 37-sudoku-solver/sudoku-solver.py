class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_move_valid(board, r, c, new_num):
            # check current row and col
            for i in range(9):
                if (board[r][i] == new_num or 
                    board[i][c] == new_num or 
                    board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == new_num):
                    return False
            return True

        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for i in range(1, 10):
                            new_num = str(i)
                            if is_move_valid(board, r, c, new_num):
                                board[r][c] = new_num
                                
                                if solve(board):
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False # if all tried and not solved
            return True # solved

        solve(board)