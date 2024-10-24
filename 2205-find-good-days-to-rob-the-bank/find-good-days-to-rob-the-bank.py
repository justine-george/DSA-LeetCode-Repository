class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # find number of non increasing days till i
        N = len(security)
        left = [0] * N
        for i in range(1, N):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1

        # find number of non decreasing days from i
        right = [0] * N
        for i in range(N - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        
        res = []
        for i in range(time, N - time):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        return res