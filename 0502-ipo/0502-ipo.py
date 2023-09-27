class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # maxheap, populate later
        maxProfit = []

        # minheap for storing capital, profit pair
        minCapital = [(capital, profit) for capital, profit in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                # populate maxProfit maxHeap
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += (heapq.heappop(maxProfit) * -1)

        return w