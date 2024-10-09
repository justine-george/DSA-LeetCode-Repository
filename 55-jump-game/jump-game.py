class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # dp solution: T: O(n**2), S: O(n)
        # dp = [False] * len(nums)
        # dp[0] = True
        # for i in range(len(nums)):
        #     if dp[i] and nums[i] > 0:
        #         for j in range(1, min(nums[i] + 1, len(nums))):
        #             dp[i + j] = True
        #             if i + j == len(nums) - 1:
        #                 return True
        # return dp[len(nums) - 1]

        # greedy solution: T: O(n), S: O(1)
        goalpost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goalpost:
                goalpost = i
        return goalpost == 0