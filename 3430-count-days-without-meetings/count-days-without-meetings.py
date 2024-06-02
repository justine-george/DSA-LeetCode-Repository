class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # merge intervals

        meetings.sort(key=lambda x: x[0])
        
        intervals = [meetings[0]]
        
        for cur_start, cur_end in meetings:
            prev_start,prev_end = intervals[-1][0], intervals[-1][1]

            # cur comes after (no overlap)
            if cur_start > prev_end:
                intervals.append([cur_start, cur_end])

            # overlap
            else:
                new_end = max(cur_end, prev_end)
                intervals[-1][1] = new_end

        # iterate over the new non overlapping intervals
        res = days
        for start, end in intervals:
            res -= (end - start + 1)
        
        return res