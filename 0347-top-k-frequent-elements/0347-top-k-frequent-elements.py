class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = Counter(nums)
        min_heap = []
        for key in c_map:
            freq = c_map[key]
            if len(min_heap) == k:
                if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, key))
            else:
                heapq.heappush(min_heap, (freq, key))
        
        res = []
        for freq, num in min_heap:
            res.append(num)
        
        return res