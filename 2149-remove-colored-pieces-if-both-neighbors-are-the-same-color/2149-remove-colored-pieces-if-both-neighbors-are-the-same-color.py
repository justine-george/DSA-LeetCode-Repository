class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count, b_count = 0, 0
        for r in range(1, len(colors) - 1):
            if colors[r] == colors[r - 1] == colors[r + 1]:
                if colors[r] == "A":
                    a_count += 1
                else:
                    b_count += 1

        return a_count > b_count

        # A A A B A B B

