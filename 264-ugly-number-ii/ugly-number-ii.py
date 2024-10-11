class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n

        ugly_heap = [1]
        visited = set([1])
        factors = [2, 3, 5]
        
        for i in range(n):
            cur = heappop(ugly_heap)

            for f in factors:
                candidate = cur * f
                if candidate not in visited:
                    heappush(ugly_heap, candidate)
                    visited.add(candidate)

        return cur


        # # dp solution
        # if n <= 5:
        #     return n

        # ugly = [1]
        
        # i2, i3, i5 = 0, 0, 0

        # for _ in range(1, n):
        #     next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        #     ugly.append(next_ugly)

        #     if next_ugly == ugly[i2] * 2:
        #         i2 += 1
        #     if next_ugly == ugly[i3] * 3:
        #         i3 += 1
        #     if next_ugly == ugly[i5] * 5:
        #         i5 += 1
        
        # return ugly[-1]