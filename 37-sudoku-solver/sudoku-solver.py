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

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for i in range(1, 10):
                            new_num = str(i)
                            if is_move_valid(r, c, new_num):
                                board[r][c] = new_num
                                
                                if solve():
                                    return True
                                
                                board[r][c] = '.'
                        return False # if all tried and not solved
            return True # solved

        solve()