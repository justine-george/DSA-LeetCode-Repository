class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        dp = {num: 1 for num in arr}
        arr.sort()
        for num in arr:
            for factor in arr:
                if factor == num:
                    break

                if num % factor == 0 and num // factor in dp:
                    dp[num] += dp[factor] * dp[num // factor]

        return sum(dp.values()) % (10 ** 9 + 7)