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
                biggest_time = -1 * heapq.heappop(heap)
                # ensures we save time by removing the lengthiest course so far
                time_lapsed -= biggest_time
        
        return len(heap)