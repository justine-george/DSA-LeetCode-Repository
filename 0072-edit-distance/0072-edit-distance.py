class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2d dp array - bottom up
        # + 1 to handle base cases
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        #     *       word2 cols
        # word1 rows

        # fill base cases
        # fill bottom most row
        for i in range(len(word2) + 1):
            cache[len(word1)][i] = len(word2) - i
        # fill right most column
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # start from 2nd last row
        for i in range(len(word1) - 1, -1, -1):
            # start from 2nd last column
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j], # delete
                        cache[i][j + 1], # insert
                        cache[i + 1][j + 1] # replace
                    )
        
        return cache[0][0]