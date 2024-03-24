class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []

        k = len(nums)
        max_val = float('-inf')

        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        res = [pq[0][0], max_val]

        while True:
            value, list_index, num_index = heapq.heappop(pq)

            if num_index == len(nums[list_index]) - 1:
                break

            next_num = nums[list_index][num_index + 1]
            heapq.heappush(pq, (next_num, list_index, num_index + 1))
            max_val = max(max_val, next_num)

            if max_val - pq[0][0] < res[1] - res[0]:
                res = [pq[0][0], max_val]
        

        return res