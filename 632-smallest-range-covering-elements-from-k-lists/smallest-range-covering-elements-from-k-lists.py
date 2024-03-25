class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        max_val = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        ans = [pq[0][0], max_val]

        while True:
            val, list_index, num_index = heapq.heappop(pq)

            if num_index == len(nums[list_index]) - 1:
                break
            
            next_num = nums[list_index][num_index + 1]
            heapq.heappush(pq, (next_num, list_index, num_index + 1))

            max_val = max(max_val, next_num)
            
            if ans[1] - ans[0] > max_val - pq[0][0]:
                ans = [pq[0][0], max_val]
        
        return ans
