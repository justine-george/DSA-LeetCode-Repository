class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem_dict = defaultdict(int)
        pair_count = 0
        for duration in time:
            if not (duration % 60):
                pair_count += rem_dict[0]
            else:
                pair_count += rem_dict[60 - (duration % 60)]

            rem_dict[duration % 60] += 1
            
        return pair_count