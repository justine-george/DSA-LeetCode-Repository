class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        l = 0
        for i in range(1, n + 1):
            res.append("Push")
            if i != target[l]:
                res.append("Pop")
            else:
                l += 1
                if l == len(target):
                    return res

        return res