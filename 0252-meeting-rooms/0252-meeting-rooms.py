class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # T: O(nlogn)
        sortedList = sorted(intervals)
        
        for i in range(1, len(sortedList)):
            print(sortedList[i - 1][1])
            if sortedList[i - 1][1] > sortedList[i][0]:
                return False
        
        return True