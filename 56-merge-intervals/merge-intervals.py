class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        new_list = [intervals[0]]
        for cur_start, cur_end in intervals[1:]:
            # if cur interval lies after prev interval
            if cur_start > new_list[-1][1]:
                new_list.append([cur_start, cur_end])
            else:
                new_list[-1][1] = max(new_list[-1][1], cur_end)

        
        return new_list