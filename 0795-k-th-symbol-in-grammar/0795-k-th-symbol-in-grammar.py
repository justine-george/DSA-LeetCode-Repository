class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        # 0110100110010110

        # 1,2 -> 1
        # 3,4 -> 2
        # 5,6 -> 3
        # 7,8 -> 4

        if k == 1:
            return 0
        elif k % 2:
            return self.kthGrammar(n - 1, (k + 1) / 2)
        else:
            val = self.kthGrammar(n - 1, k / 2)
            return 0 if val else 1