class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3

        def getWinner(map):
            if map["A"] == 3:
                return "A"
            elif map["B"] == 3:
                return "B"
            else:
                return None
 
        # form the grid
        grid = [[""] * n for i in range(n)]
        for i in range(len(moves)):
            row_i, col_i = moves[i]
            # A's turn
            if i % 2 == 0:
                grid[row_i][col_i] = "A"
            # B's turn
            else:
                grid[row_i][col_i] = "B"

        # check all the possibilities
        for i in range(n):
            rowset = {"A": 0, "B": 0}
            colset = {"A": 0, "B": 0}
            for j in range(n):
                # check all rows
                if grid[i][j] != "":
                    rowset[grid[i][j]] += 1
                # check all cols
                if grid[j][i] != "":
                    colset[grid[j][i]] += 1

            winner = getWinner(rowset)
            if winner: return winner

            winner = getWinner(colset)
            if winner: return winner
        
        # Check diagonals outside the nested loop
        posdiag = {"A": 0, "B": 0}
        negdiag = {"A": 0, "B": 0}
        for i in range(n):
            if grid[i][n - 1 - i] != "":
                posdiag[grid[i][n - 1 - i]] += 1
            if grid[i][i] != "":
                negdiag[grid[i][i]] += 1

        winner = getWinner(posdiag)
        if winner: return winner
        
        winner = getWinner(negdiag)
        if winner: return winner
        
        return "Draw" if len(moves) == 9 else "Pending"