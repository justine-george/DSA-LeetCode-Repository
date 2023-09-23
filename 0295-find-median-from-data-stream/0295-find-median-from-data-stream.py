class MedianFinder:

    def __init__(self):
        # two heaps, small, large = maxHeap, minHeap
        # heap sizes should not differ more than 1
        self.small, self.large = [], []

    # helper function to move top from source to dest
    def moveSourceDest(self, source, dest, fromMaxHeap = False):
        val = heapq.heappop(source)
        if fromMaxHeap:
            val = -1 * val
            heapq.heappush(dest, val)
        else:
            heapq.heappush(dest, -1 * val)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        # if max value in small is greater than min value in large
        if (
            self.small
            and self.large 
            and (-1 * self.small[0]) > self.large[0]):
            self.moveSourceDest(self.small, self.large, True)
        
        # uneven cases
        if len(self.small) > len(self.large) + 1:
            self.moveSourceDest(self.small, self.large, True)
        
        if len(self.large) > len(self.small) + 1:
            self.moveSourceDest(self.large, self.small)

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