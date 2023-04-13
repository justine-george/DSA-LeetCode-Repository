class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(klogn) heap approach
        freq = collections.defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
            
        maxHeap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(maxHeap)
            
        # Note: pop from the heap k times to get top k frequent elements
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res
    
    
#         # T: O(n) using bucket sort with a twist
#         # array indexed by count and value is a list of numbers with this count
#         countDict = {}
        
#         maxCount = 0
#         for n in nums:
#             countDict[n] = 1 + countDict.get(n, 0)
#             maxCount = max(maxCount, countDict[n])
        
#         # make bucket of size max count
#         bucket = [[] for i in range(maxCount)]
        
#         for num, freq in countDict.items():
#             bucket[freq - 1].append(num)
        
#         res = []
#         for i in range(len(bucket) - 1, -1, -1):
#             for n in bucket[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res