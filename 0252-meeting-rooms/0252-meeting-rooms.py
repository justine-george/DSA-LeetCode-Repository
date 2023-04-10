class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # T: O(nlogn)
        # no change to the input list
        # sortedList = sorted(intervals)
        
        # but this one mutates the input
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        
        return True