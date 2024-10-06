class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # similar to LCS, make 2d array
        # len(word1) + 1 * len(word2) + 1
        cache = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # base case bottom row
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        
        # base case right column
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        print(cache)

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])

        return cache[0][0]