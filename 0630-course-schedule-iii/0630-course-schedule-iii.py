class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])

        heap = []

        timeSoFar = 0

        for duration, lastDay in courses:
            # max heap
            heapq.heappush(heap, -duration)
            timeSoFar += duration

            if timeSoFar > lastDay:
                biggestDuration = -1 * heapq.heappop(heap)
                timeSoFar -= biggestDuration
        
        return len(heap)