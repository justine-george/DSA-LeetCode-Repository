class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        score = defaultdict(int)

        for f, t, a in transactions:
            score[f] -= a
            score[t] += a
        
        positives = [val for val in score.values() if val > 0]
        negatives = [val for val in score.values() if val < 0]

        def recurse(positives, negatives):
            # we have satisfied all the nodes
            if len(positives) + len(negatives) == 0:
                return 0

            neg = negatives[0]
            count = inf

            for pos in positives:
                new_positives = positives.copy()
                new_negatives = negatives.copy()

                # we want to reduce the number of nodes
                new_positives.remove(pos)
                new_negatives.remove(neg)

                # best possible case
                if pos == -neg:
                    pass
                # give out all and clear debt, but receiver yet to receive little more
                elif pos > -neg:
                    new_positives.append(pos+neg)
                # receiver got all, but a little more money to give out for the person in debt
                else:
                    new_negatives.append(pos+neg)
                
                count = min(count, recurse(new_positives, new_negatives))
            
            return count + 1
        
        return recurse(positives, negatives)