class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def get_score(scores):
            total_score = 0
            for i, score in enumerate(scores):
                if (i >= 2 and (scores[i - 2] == 10 or scores[i - 1] == 10)) or (i == 1 and scores[i - 1] == 10):
                    total_score += (2 * score)
                else:
                    total_score += score
            return total_score

        player_1_score = get_score(player1)
        player_2_score = get_score(player2)

        if player_1_score > player_2_score:
            return 1
        elif player_1_score < player_2_score:
            return 2
        else:
            return 0