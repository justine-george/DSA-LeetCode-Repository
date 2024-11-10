class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS_from_index = [1] * N

        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    LIS_from_index[i] = max(LIS_from_index[i], 1 + LIS_from_index[j])
        
        return max(LIS_from_index)