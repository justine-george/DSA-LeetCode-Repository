class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # T: O(n), S: O(1) solution
        ugly_list = [1]
        i2 = i3 = i5 = 0
        for i in range(n - 1):
            next_ugly = min(ugly_list[i2] * 2, ugly_list[i3] * 3, ugly_list[i5] * 5)
            ugly_list.append(next_ugly)

            if next_ugly == ugly_list[i2] * 2:
                i2 += 1
            if next_ugly == ugly_list[i3] * 3:
                i3 += 1
            if next_ugly == ugly_list[i5] * 5:
                i5 += 1
        
        return ugly_list[-1]
        '''
        # heap solution
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
        '''