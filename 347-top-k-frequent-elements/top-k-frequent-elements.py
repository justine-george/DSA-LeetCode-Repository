class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Bucket sort
        # # T: O(n), S: O(n)
        # freq = [[] for i in range(len(nums) + 1)]
        # c_map = Counter(nums)
        # for num, c in c_map.items():
        #     freq[c].append(num)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        
        # T: O(NlogK), S: O(K)
        c_map = Counter(nums)
        min_heap = []
        for key, freq in c_map.items():
            heapq.heappush(min_heap, (freq, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]