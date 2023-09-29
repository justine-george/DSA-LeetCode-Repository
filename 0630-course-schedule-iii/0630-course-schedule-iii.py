class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # T: O(nlogn), S: O(n)
        # Approach: Greedily try to minimize time_lapsed by:
            # 1. picking courses from a list sorted by lastDay 
            # 2. add it to the maxheap of durations
            # 3. if adding any course makes time_lapsed > its deadline, then:
                #  pop from heap and reduce it from the time_lapsed

        # sort by lastDay
        courses.sort(key=lambda x:x[1])

        # add to maxheap of times
        heap = []
        time_lapsed = 0

        for time, deadline in courses:
            heapq.heappush(heap, -time)
            time_lapsed += time

            if time_lapsed > deadline:
                # ensures we save time by removing the lengthiest course so far
                time_lapsed -= (-1 * heapq.heappop(heap))
        
        return len(heap)

        # # T: O(n*d), S: O(n*d) - wont work here, memory exceeded
        # # n - len(courses), d - max value of the time_lapsed
        # memo = {}
        # def backtrack(i, time_lapsed):
        #     if i == len(courses):
        #         return 0
            
        #     if (i, time_lapsed) in memo:
        #         return memo[(i, time_lapsed)]
            
        #     taken_count = 0
        #     if time_lapsed + courses[i][0] <= courses[i][1]:
        #         taken_count = 1 + backtrack(i + 1, time_lapsed + courses[i][0])
            
        #     not_taken_count = backtrack(i + 1, time_lapsed)
        #     memo[(i, time_lapsed)] = max(taken_count, not_taken_count)
        #     return memo[(i, time_lapsed)]

        # courses.sort(key = lambda x: x[1])
        # return backtrack(0, 0)