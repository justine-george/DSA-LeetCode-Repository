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
                    # continuing from the best dot product up to the previous elements and including the current pair's dot product
                    nums1[i - 1] * nums2[j - 1] + dp[i - 1][j - 1],

                    # starting a new subsequence with only the current pair of elements
                    nums1[i - 1] * nums2[j - 1],
                    
                    # using the best dot product that does not include the current element of nums1
                    dp[i - 1][j],
                    
                    # using the best dot product that does not include the current element of nums2
                    dp[i][j - 1]
                )

        # 3. return max dot product for the entire sequence
        return dp[m][n]

        # # Top down recursiion - memoized

        # m, n = len(nums1), len(nums2)
        # memo = {}
        # def dp(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if i == m or j == n:
        #         return 0

        #     memo[(i, j)] = max(
        #         nums1[i] * nums2[j] + dp(i + 1, j + 1),
        #         dp(i + 1, j),
        #         dp(i, j + 1)
        #     )
        #     return memo[(i, j)]

        # # edge cases, when one from nums1 and one from nums2 multiply to get negative, dp() returns 0, but we need to use atleast 1 from either
        # if max(nums1) < 0 and min(nums2) > 0:
        #     return max(nums1) * min(nums2)
        # if max(nums2) < 0 and min(nums1) > 0:
        #     return max(nums2) * min(nums1)
        
        # return dp(0, 0)