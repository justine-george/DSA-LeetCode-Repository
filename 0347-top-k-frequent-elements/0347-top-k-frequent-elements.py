class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
            
        minHeap = [(count, num) for num, count in freq.items()]
        heapq.heapify(minHeap)
        
        # remove least frequent elements, so that remaining elements are top k frequent
        while len(minHeap) > k:
            heapq.heappop(minHeap)
            
        # another approach is to make a maxHeap and pop from the heap k times to get top k frequent elements
        
        res = []
        for count, n in minHeap:
            res.append(n)
        return res