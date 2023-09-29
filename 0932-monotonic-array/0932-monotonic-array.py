class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # T: O(n), S: O(1)
        incr, decr = True, True

        for i, n in enumerate(nums):
            if not incr and not decr:
                return False

            # increasing
            if incr and i > 0 and nums[i - 1] > n:
                incr = False

            # decreasing
            if decr and i > 0 and nums[i - 1] < n:
                decr = False
        
        return incr or decr