class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * prefix)
            prefix = res[i]
            
        postfix = 1
        for i, el in reversed(list(enumerate(nums))):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        
        return res