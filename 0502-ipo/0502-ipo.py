class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 2 heap pattern
        # T: O(nlogn)
        # S: O(n)

        # maxheap
        maxProfit = [] # store affordable projects based on the capital value from the capital minheap

        # min heap, based on capital value. [0] th value would be min capital pair
        minCapital = [(capital, profit) for capital, profit in zip(capital, profits)]
        heapq.heapify(minCapital)

        # do k times
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                # populate affordable projects in maxProfit maxheap
                min_c, p_for_c = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p_for_c)
            # in case we don't have k profits available
            if not maxProfit:
                break
            w += (-1 * heapq.heappop(maxProfit))

        return w