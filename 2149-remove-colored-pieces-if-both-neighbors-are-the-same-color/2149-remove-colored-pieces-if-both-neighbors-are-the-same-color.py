class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # figure out number of moves
        a_moves, b_moves = 0, 0
        l = 0
        for r in range(len(colors)):
            if colors[l] != colors[r]:
                l = r
            
            extra = r - l + 1 - 2
            if extra > 0:
                if colors[l] == 'A':
                    a_moves += 1
                else:
                    b_moves += 1
        
        # alice wins if a_moves > b_moves
        return a_moves > b_moves