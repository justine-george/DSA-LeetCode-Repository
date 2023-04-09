class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        # remove all elements until heap size is k
        # self.minHeap[0] now contains kth largest number
        # maintain this property in self.add(val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        # remove all elements until heap size is k
        # self.minHeap[0] now contains kth largest number
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # get the kth largest element
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)