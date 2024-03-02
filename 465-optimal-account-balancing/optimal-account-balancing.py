from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        score = defaultdict(int)
        for f, t, amount in transactions:
            score[f] += amount
            score[t] -= amount
        
        positives = [v for v in score.values() if v > 0]
        negatives = [v for v in score.values() if v < 0]

        dp = {}
        def recurse(positives, negatives):
            if len(positives) + len(negatives) == 0:
                return 0

            key = tuple(sorted(positives)), tuple(sorted(negatives))
            if key in dp:
                return dp[key]
    
            negative = negatives[0]
            count = inf

            for positive in positives:
                new_positives = positives.copy()
                new_negatives = negatives.copy()

                new_positives.remove(positive)
                new_negatives.remove(negative)

                if positive == -negative:
                    pass
                elif positive > -negative:
                    new_positives.append(positive + negative)
                else:
                    new_negatives.append(positive + negative)
                
                count = min(count, recurse(new_positives, new_negatives))

            dp[key] = count + 1
            return count + 1

        return recurse(positives, negatives)