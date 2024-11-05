class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        def check(val):
            temp = val
            for n in nums:
                temp += n
                if temp < 1:
                    return False
            return True
        
        l, r = 1, 100 * 100 + 1
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l