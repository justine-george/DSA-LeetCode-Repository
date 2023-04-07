class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * prefix
            prefix = res[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix # res[i] is the prefix
            postfix = postfix * nums[i]

        
        return res