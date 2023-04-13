class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # T: O(klogn) heap approach
#         freq = collections.defaultdict(lambda: 0)
#         for n in nums:
#             freq[n] += 1
            
#         minHeap = [(count, num) for num, count in freq.items()]
#         heapq.heapify(minHeap)
        
#         # remove least frequent elements, so that remaining elements are top k frequent
#         while len(minHeap) > k:
#             heapq.heappop(minHeap)
            
#         # Note: another approach is to make a maxHeap and pop from the heap k times to get top k frequent elements
        
#         res = []
#         for count, n in minHeap:
#             res.append(n)
#         return res
    
    
        # T: O(n) using bucket sort with a twist
        # array indexed by count and value is a list of numbers with this count
        freq = collections.defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
        
        # make bucket of size max count
        bucket = [[] for i in range(len(nums))]
        
        for num, count in freq.items():
            bucket[count - 1].append(num)
        
        res = []
        count = k
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) != 0:
                res.extend(bucket[i])
                count -= len(bucket[i])
            if count == 0:
                break
        return res
                
        
        