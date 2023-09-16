class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Helper function to get sum of digits
        def getSumDigits(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        # A dictionary to store the maximum and second maximum values for each sum of digits
        map = {}
        
        for n in nums:
            sum_digits = getSumDigits(n)
            if sum_digits in map:
                if n > map[sum_digits][0]:
                    map[sum_digits] = [n, map[sum_digits][0]]
                elif n > map[sum_digits][1]:
                    map[sum_digits][1] = n
            else:
                map[sum_digits] = [n, 0]
        
        res = max((map[key][0] + map[key][1] for key in map if map[key][1] > 0), default=-1)
        return res
