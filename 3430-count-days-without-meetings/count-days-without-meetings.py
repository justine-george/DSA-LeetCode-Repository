class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # merge intervals first
        meetings.sort(key=lambda x: x[0])
        new_list = [meetings[0]]
        for cur_start, cur_end in meetings:
            prev_start,prev_end = new_list[-1][0], new_list[-1][1]

            # current interval comes after prev interval
            if cur_start > prev_end:
                new_list.append([cur_start, cur_end])
            # overlap
            else:
                new_end = max(cur_end, prev_end)
                new_list[-1][1] = new_end

        # iterate over the new non overlapping intervals
        res = days
        for start, end in new_list:
            res -= (end - start + 1)
        
        return res