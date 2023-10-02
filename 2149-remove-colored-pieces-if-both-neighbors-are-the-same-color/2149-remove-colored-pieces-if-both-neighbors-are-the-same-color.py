class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # figure out number of moves
        a_moves, b_moves = 0, 0

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a_moves += 1
                else:
                    b_moves += 1
        
        # alice wins if a_moves > b_moves
        return a_moves > b_moves