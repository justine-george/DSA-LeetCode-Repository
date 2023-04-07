class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        
        # T: O(n), S:O(1) - (DP) We use currMin and currMax
        # of i-1th position to find out the same for ith position
        currMin, currMax = 1, 1
        for n in nums:
            temp = currMax
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp * n, currMin * n, n)
            res = max(res, currMax)
            
        return res