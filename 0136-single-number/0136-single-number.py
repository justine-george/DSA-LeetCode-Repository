class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR all numbers - what's left is the single number
        # XOR - inequality checker
        # For ex. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        res = 0
        for n in nums:
            res = n ^ res
        return res