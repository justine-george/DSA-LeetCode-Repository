class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {c: [0]*len(votes[0]) + [c] for c in votes[0]}

        for vote in votes:
            for i, char in enumerate(vote):
                count[char][i] -= 1
        
        return "".join(sorted(votes[0], key=count.get))