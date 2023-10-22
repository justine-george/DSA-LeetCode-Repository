class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cMap = Counter(nums)

        if len(cMap) == 1:
            return 1

        def search(i):
            ans = 0
            for key in cMap:
                rem = cMap[key] % i
                if rem > cMap[key] // i:
                    return 0
                ans += ceil(cMap[key] / (i + 1))

            return ans

        min_val, max_val = 1, min(cMap.values())
        res = float('inf')
        for i in range(min_val, max_val + 1):
            val = search(i)
            if val:
                res = min(res, val)
        return res



        # max_heap = []
        # for c_val in cMap.values():
        #     max_val = max(max_val, c_val)
        #     min_val = min(min_val, c_val)
        #     heapq.heappush(max_heap, -c_val)
            
        # while max_heap and max_val - min_val > 1:
        #     cur_max = -1 * heapq.heappop(max_heap)
            
        #     i = 2
        #     while (cur_max // i) - min_val > 1:
        #         i += 1
            
        #     min_val = min(min_val, cur_max // i, cur_max - (cur_max // i))
            
        #     if cur_max % i != 0:
        #         heapq.heappush(max_heap, - (cur_max % i))
            
        #     while i > 0:
        #         heapq.heappush(max_heap, - (cur_max // i))
        #         i -= 1
            
        #     max_val = -1 * max_heap[0]
        
        # return len(max_heap)