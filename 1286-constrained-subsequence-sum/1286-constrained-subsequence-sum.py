class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = nums[0]
        max_heap = [(-nums[0], 0)] # max_sum, index

        for i in range(1, len(nums)):
            while i - max_heap[0][1] > k:
                heapq.heappop(max_heap)

            cur_max = max(nums[i], nums[i] - max_heap[0][0])
            heapq.heappush(max_heap, (-cur_max, i))
            res = max(res, cur_max)
        
        return res
        
        # # T: O(nk), s: O(n) not optimal here, TLE
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     dp[i] = nums[i]
        #     for j in range(max(0, i - k), i):
        #         dp[i] = max(dp[i], nums[i] + dp[j])
        
        # return max(dp)