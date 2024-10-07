class Solution:
    def jump(self, nums: List[int]) -> int:
        # # nums:[2,3,1,1,4]
        # # dp:  [0,1,1,2,2]
        # # dp approach
        # # T: O(n**2), S: O(n)
        # dp = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i + 1, i + nums[i] + 1):
        #         if j < len(nums):
        #             if dp[j] == 0:
        #                 dp[j] = dp[i] + 1
        #             else:
        #                 dp[j] = min(dp[j], dp[i] + 1)
        
        # return dp[len(nums) - 1]

        # greedy approach
        # T: O(n), S:O(1)
        # think in terms of BFS, with a l, r boundary
        # each index's spread forms the next level of BFS
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            res += 1
            l = r + 1
            r = farthest
        return res


        