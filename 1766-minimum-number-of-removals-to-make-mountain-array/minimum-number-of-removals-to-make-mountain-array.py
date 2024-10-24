class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # LIS[i] -> lis ending at i
        def get_LIS(nums):
            LIS = [1] * len(nums)
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:
                        LIS[i] = max(LIS[i], 1 + LIS[j])
            return LIS
        
        # LDS[i] -> lds starting at i
        def get_LDS(nums):
            LDS = [1] * len(nums)
            for i in range(len(nums) - 2, -1, -1):
                for j in range(i + 1, len(nums)):
                    if nums[i] > nums[j]:
                        LDS[i] = max(LDS[i], 1 + LDS[j])
            return LDS

        
        lis = get_LIS(nums)
        lds = get_LDS(nums)

        max_sum = 0
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1 and lis[i] > 1 and lds[i] > 1:
                max_sum = max(max_sum, lis[i] + lds[i] - 1)

        return len(nums) - max_sum