class MedianFinder:

    def __init__(self):
        # two heaps, small, large = maxHeap, minHeap
        # heap sizes should not differ more than 1
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        # if max value in small is greater than min value in large
        if (
            self.small
            and self.large 
            and (-1 * self.small[0]) > self.large[0]):
            # move this value to the large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven case, small is longer
        if len(self.small) > len(self.large) + 1:
            # move this value to the large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven case, large is longer
        if len(self.large) > len(self.small) + 1:
            # move this value to the small heap
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # equal length, take the mean of both heaps top values
        return ((-1 * self.small[0]) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()