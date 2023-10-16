class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = [1, 1]
        l = 2
        while l <= rowIndex:
            cur = [1] * (l + 1)
            for i in range(1, l):
                cur[i] = prev[i - 1] + prev[i]
            prev = cur
            l += 1

        return prev