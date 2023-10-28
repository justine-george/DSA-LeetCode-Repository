class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prev = [1] * 5
        for i in range(2, n + 1):
            cur = [0] * 5
            for j in range(5):
                if j == 0:
                    cur[0] = prev[1] + prev[2] + prev[4]
                elif j == 1:
                    cur[1] = prev[0] + prev[2]
                elif j == 2:
                    cur[2] = prev[1] + prev[3]
                elif j == 3:
                    cur[3] = prev[2]
                else:
                    cur[4] = prev[2] + prev[3]
            prev = cur

        return sum(prev) % (10 ** 9 + 7)