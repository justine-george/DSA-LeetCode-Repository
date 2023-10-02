class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # figure out number of moves
        a_moves = 0
        b_moves = 0
        isA = colors[0] == "A"
        start = 0
        i = 1
        while i < len(colors):
            if isA:
                if colors[i] != colors[i - 1]:
                    # calculate length of A
                    if i - start >= 3:
                        a_moves += (i - start) - 2
                    isA = False
                    start = i
            else:
                if colors[i] != colors[i - 1]:
                    # calculate length of B
                    if i - start >= 3:
                        b_moves += (i - start) - 2
                    isA = True
                    start = i
            i += 1

        if i - start >= 3:
            if isA:
                a_moves += (i - start) - 2
            else:
                b_moves += (i - start) - 2
        
        return a_moves > b_moves