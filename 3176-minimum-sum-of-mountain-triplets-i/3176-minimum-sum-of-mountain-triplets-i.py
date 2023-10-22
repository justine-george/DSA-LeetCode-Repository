class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        res = min(res, nums[i] + nums[j] + nums[k])
        
        return res if res != float('inf') else -1