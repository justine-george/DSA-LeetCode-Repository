class Solution:
    def generate(self, numRows: int) -> List[List[int]]:    
        # 1
        # 11
        # 121
        # 1331
        res = []
        for i in range(1, numRows + 1):
            if i < 3:
                res.append([1 for _ in range(i)])
                continue
            temp = [1]
            for j in range(1, i - 1):
                temp.append(res[-1][j - 1] + res[-1][j])
            temp += [1]
            res.append(temp)
        return res

