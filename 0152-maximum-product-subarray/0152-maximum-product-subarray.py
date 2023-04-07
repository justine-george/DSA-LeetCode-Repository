class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # T: O(n), S:O(1) - (DP) We use currMin and currMax
        # of i-1th position to find out the same for ith position
        currMin = currMax = res = nums[0]
        for n in nums[1:]:
            currMax, currMin = max(currMax * n, currMin * n, n), min(currMax * n, currMin * n, n)
            res = max(res, currMax)
        return res