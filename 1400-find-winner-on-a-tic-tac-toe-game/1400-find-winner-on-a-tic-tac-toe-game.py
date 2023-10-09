class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # better solution
        n = 3
        rows, cols = [0] * n, [0] * n
        d1, d2 = 0, 0
        player = 1 # other player is -1, player 1 starts the game
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c: d1 += player
            if r == n - 1 - c: d2 += player
            # if there is a winner
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                return "A" if player == 1 else "B"
            # flip the player
            player *= -1
        
        return "Draw" if len(moves) == (n * n) else "Pending"

        # n = 3

        # def getWinner(map):
        #     if map["A"] == 3:
        #         return "A"
        #     elif map["B"] == 3:
        #         return "B"
        #     else:
        #         return None
 
        # # form the grid
        # grid = [[""] * n for i in range(n)]
        # for i in range(len(moves)):
        #     row_i, col_i = moves[i]
        #     # A's turn
        #     if i % 2 == 0:
        #         grid[row_i][col_i] = "A"
        #     # B's turn
        #     else:
        #         grid[row_i][col_i] = "B"

        # # check all the possibilities
        # for i in range(n):
        #     rowset = {"A": 0, "B": 0}
        #     colset = {"A": 0, "B": 0}
        #     for j in range(n):
        #         # check all rows
        #         if grid[i][j] != "":
        #             rowset[grid[i][j]] += 1
        #         # check all cols
        #         if grid[j][i] != "":
        #             colset[grid[j][i]] += 1

        #     winner = getWinner(rowset)
        #     if winner: return winner

        #     winner = getWinner(colset)
        #     if winner: return winner
        
        # # Check diagonals outside the nested loop
        # posdiag = {"A": 0, "B": 0}
        # negdiag = {"A": 0, "B": 0}
        # for i in range(n):
        #     if grid[i][n - 1 - i] != "":
        #         posdiag[grid[i][n - 1 - i]] += 1
        #     if grid[i][i] != "":
        #         negdiag[grid[i][i]] += 1

        # winner = getWinner(posdiag)
        # if winner: return winner
        
        # winner = getWinner(negdiag)
        # if winner: return winner
        
        # return "Draw" if len(moves) == 9 else "Pending"