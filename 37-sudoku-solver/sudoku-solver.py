class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_move_valid(r, c, new_num):
            # check current row and col
            for i in range(9):
                if board[r][i] == new_num or board[i][c] == new_num:
                    return False

            # check 3x3
            start_row, start_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == new_num:
                        return False
            
            return True

        rset = {i: set() for i in range(9)}
        cset = {i: set() for i in range(9)}
        gset = {(r, c) for r in range(3) for c in range(3)}
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for new_num in map(str, range(1, 10)):
                            if is_move_valid(r, c, new_num):
                                board[r][c] = new_num
                                
                                if solve():
                                    return True
                                
                                board[r][c] = '.'
                        return False # if all tried and not solved
            return True # solved

        solve()