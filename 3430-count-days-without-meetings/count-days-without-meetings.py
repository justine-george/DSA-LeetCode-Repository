class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # merge intervals
        intervals = []
        
        meetings.sort(key=lambda x: x[0])
        for start, end in meetings:
            if not intervals:
                intervals.append((start, end))
                continue

            recent_start,recent_end = intervals[-1][0], intervals[-1][1]

            # cur comes after or before (no overlap)
            if start > recent_end or recent_start > end:
                intervals.append((start, end))

            # overlap
            else:
                intervals.pop()
                new_start = min(start, recent_start)
                new_end = max(end, recent_end)
                intervals.append((new_start, new_end))

        
        # iterate over the new non overlapping intervals and sum all dates
        res = days
        for start, end in intervals:
            res -= (end - start + 1)
        
        return res