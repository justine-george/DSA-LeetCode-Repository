class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by deadline
        courses.sort(key=lambda x:x[1])

        # add to maxheap, check condition < or > deadline
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