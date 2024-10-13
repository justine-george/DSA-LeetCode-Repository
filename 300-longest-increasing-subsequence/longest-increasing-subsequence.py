class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [1] * N

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)