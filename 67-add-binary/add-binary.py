class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        res = []
        carry = 0
        for i in range(max_len - 1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            carry = sum // 2
            res.append(str(sum % 2))
        
        if carry:
            res.append('1')

        return ''.join(reversed(res))