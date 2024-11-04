class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rev_a, rev_b = a[::-1], b[::-1]
        res = []
        carry = 0
        i = 0
        while i < len(a) or i < len(b):
            ans = (int(rev_a[i]) if i < len(a) else 0) + (int(rev_b[i]) if i < len(b) else 0) + carry
            if ans == 2:
                ans = 0
                carry = 1
            elif ans == 3:
                ans = 1
                carry = 1
            else:
                carry = 0

            res.append(ans)
            i += 1
        
        if carry:
            res.append(1)
        
        res.reverse()
        return ''.join(str(num) for num in res)