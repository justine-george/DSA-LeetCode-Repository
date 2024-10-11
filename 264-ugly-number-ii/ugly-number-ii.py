class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        heap solution
        '''
        min_heap = [1]
        visited = set([1])
        factors = [2, 3, 5]
        last_popped = 1
        for i in range(n):
            last_popped = heapq.heappop(min_heap)
            for f in factors:
                candidate = f * last_popped
                if candidate not in visited:
                    visited.add(candidate)
                    heapq.heappush(min_heap, candidate)

        return last_popped