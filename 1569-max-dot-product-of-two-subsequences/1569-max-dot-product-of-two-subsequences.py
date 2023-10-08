class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # 1. initialization
        # max dot product of non-empty subsequences upto i, j (not included)
        dp = [[float('-inf')] * (n + 1) for i in range(m + 1)]

        # 2. update
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1] + dp[i - 1][j - 1],
                    nums1[i - 1] * nums2[j - 1],
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

        # 3. return
        return dp[m][n]