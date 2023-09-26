class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # bottom up dp
        # cache = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text1) + 1)
        curr = [0] * (len(text1) + 1)

        for j in range(len(text2) - 1, -1, -1):
            for i in range(len(text1) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # we go diagonally since we can skip this i and j
                    # cache[i][j] = 1 + cache[i + 1][j + 1]
                    curr[i] = 1 + prev[i + 1]
                else:
                    # cache[i][j] = max(
                    #     cache[i + 1][j],
                    #     cache[i][j + 1]
                    #     )
                    curr[i] = max(curr[i + 1], prev[i])
            prev, curr = curr, prev 
        
        # return cache[0][0]
        return prev[0]