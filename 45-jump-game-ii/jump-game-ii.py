class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    if dp[j] == 0:
                        dp[j] = dp[i] + 1
                    else:
                        dp[j] = min(dp[j], dp[i] + 1)
                if j == len(nums) - 1:
                    return dp[j]
        
        return dp[len(nums) - 1]


        # [2,3,1,1,4]
        # [0,1,1,2,2]