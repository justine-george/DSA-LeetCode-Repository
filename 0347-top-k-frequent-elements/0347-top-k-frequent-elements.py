class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
        
        heap = []
        for key in freq:
            heap.append((freq[key], key))
        
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        
        res = []
        for count, n in heap:
            res.append(n)
        return res