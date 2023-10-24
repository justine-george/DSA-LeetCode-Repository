class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        # T: O(n), S: O(n)
        freq = [[] for i in range(len(nums) + 1)]
        c_map = Counter(nums)
        for num, c in c_map.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        # # T: O(NlogN), S: O(K)
        # c_map = Counter(nums)
        # min_heap = []
        # for key in c_map:
        #     freq = c_map[key]
        #     if len(min_heap) == k:
        #         if freq > min_heap[0][0]:
        #             heapq.heappop(min_heap)
        #             heapq.heappush(min_heap, (freq, key))
        #     else:
        #         heapq.heappush(min_heap, (freq, key))
        
        # res = []
        # for freq, num in min_heap:
        #     res.append(num)
        
        # return res