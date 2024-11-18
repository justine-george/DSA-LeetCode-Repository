class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # fill 0, n - 1 elements with (x,y) values - y in the 10 LS bits, and x in the following bits
        for i in range(n):
            nums[i] <<= 10
            nums[i] |= nums[i + n]
        
        # now use these values to fill x and y values from back to front
        ones = ((2 ** 10) - 1)
        j = 2*n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & ones
            x = nums[i] >> 10

            nums[j] = y
            nums[j - 1] = x
            j -= 2 
        
        return nums