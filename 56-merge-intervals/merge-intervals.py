class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_list = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = merged_list[-1]
            new_start, new_end = intervals[i]

            # check if overlap:
            if prev_end >= new_start:
                merged_list.pop()
                new_start = min(prev_start, new_start)
                new_end = max(prev_end, new_end)
            
            merged_list.append([new_start, new_end])

        return merged_list