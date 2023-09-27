class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for k in range(numRows):
            # length is k + 1
            row = [1] * (k + 1)

            # beginning and end is always 1
            row[0] = row[-1] = 1

            # update values in between using the row above
            # e.g for k = 2, ie. 3rd row, this loop should run 1 time
            # index from 1 
            for i in range(1, k):
                row[i] = res[-1][i - 1] + res[-1][i]
            
            # add row to the result
            res.append(row)

        return res

        # res = []
        # for k in range(1, numRows + 1):
        #     if k == 1:
        #         res.append([1])
        #     elif k == 2:
        #         res.append([1, 1])
        #     else:
        #         ans = [1]
        #         for i in range(k - 2):
        #             ans.append(res[-1][i] + res[-1][i + 1])
        #         ans.append(1)
        #         res.append(ans)
        # return res

        # i = 1
        # [1]

        # i = 2
        # [[1], [1, 1]]

        # i = 3
        # [
        #     [1],
        #     [1, 1],
        #     [1, 2, 1],
        #     [1, 3, 3, 1],
        # ]