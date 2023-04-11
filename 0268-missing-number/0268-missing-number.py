class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # works, but could run into overflow
        # n = len(nums)
        # return (n*(n + 1)//2) - sum(nums)
    
        # XOR solution - more efficient
        # [0, 1, 2, 3] ^ [0, 1, 3] = missing no. remains
        # since we are iterating from 0 to end - 1, we initialize with end value and start accumulating XOR
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res