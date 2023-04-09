class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while maxHeap:
            val1 = -heapq.heappop(maxHeap)
            if not maxHeap:
                return val1
            
            val2 = -heapq.heappop(maxHeap)
            
            diff = val1 - val2
            
            if diff == 0:
                continue
            else:
                heapq.heappush(maxHeap, -diff)
        
        return 0