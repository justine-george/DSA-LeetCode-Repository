class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {chr(i): [0]*len(votes[0]) + [i] for i in range(ord('A'), ord('Z') + 1)}

        for vote in votes:
            for i, char in enumerate(vote):
                count[char][i] += 1
        
        sorted_order = sorted(count.values(), key=lambda x: tuple(-x[i] for i in range(len(x)-1)) + (x[-1],))

        res = []
        for i in range(len(votes[0])):
            res.append(chr(sorted_order[i][-1]))

        return "".join(res)