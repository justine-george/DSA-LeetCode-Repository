class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR all numbers - what's left is the single number
        res = 0
        for n in nums:
            res = n ^ res
        return res
                
 