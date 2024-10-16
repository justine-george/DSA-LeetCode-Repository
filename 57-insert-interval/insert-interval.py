class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        res = []

        for i, interval in enumerate(intervals):
            # new interval lies before
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval lies after
            elif interval[1] < newInterval[0]:
                res.append(interval)
            # overlap
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        res.append(newInterval)
        return res
        '''
        res = []
        for i, interval in enumerate(intervals):
            # new interval before
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # new interval after
            elif interval[1] < newInterval[0]:
                res.append(interval)

            # overlap
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        res.append(newInterval)
        return res