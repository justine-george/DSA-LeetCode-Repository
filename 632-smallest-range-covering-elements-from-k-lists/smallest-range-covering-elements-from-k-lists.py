class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        #    4,   10,  15,        24,26
        # 0,    9,   12,    20
        #     5,         18,   22,     30

        # sliding window of size k, then bump up min and max (min using priority queue), calculate min(range) and ranges themselves

        pq = [] # (small number, list index, nums index)
        n = len(nums)
        max_val = float('-inf')
        
        # populate initial state
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0)) # first value from k lists
            max_val = max(max_val, nums[i][0])
        
        # initialize ans with first interval
        ans = [pq[0][0], max_val]

        while True:
            _, list_index, num_index = heapq.heappop(pq)

            # if current smallest number is the last item in its list
            if num_index == len(nums[list_index]) - 1:
                break
            
            next_number = nums[list_index][num_index + 1]
            max_val = max(max_val, next_number)
            heapq.heappush(pq, (next_number, list_index, num_index + 1))

            if max_val - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0], max_val]

        return ans
            


