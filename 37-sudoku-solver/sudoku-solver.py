class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for new_num in map(str, range(1, 10)):
                            if new_num not in rset[r] and new_num not in cset[c] and new_num not in gset[(r // 3, c // 3)]:
                            # if is_move_valid(r, c, new_num):
                                board[r][c] = new_num
                                rset[r].add(new_num)
                                cset[c].add(new_num)
                                gset[(r // 3, c // 3)].add(new_num)
                                
                                if solve():
                                    return True
                                
                                board[r][c] = '.'
                                rset[r].remove(new_num)
                                cset[c].remove(new_num)
                                gset[(r // 3, c // 3)].remove(new_num)
                        return False # if all tried and not solved
            return True # solved

        # populate rset, cset, gset before solving the board
        rset = {i: set() for i in range(9)}
        cset = {i: set() for i in range(9)}
        gset = {(r, c): set() for r in range(3) for c in range(3)}
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    new_num = board[r][c]
                    rset[r].add(new_num)
                    cset[c].add(new_num)
                    gset[(r // 3, c // 3)].add(new_num)

        solve()