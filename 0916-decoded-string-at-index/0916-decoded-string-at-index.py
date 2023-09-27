class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # find out length
        decoded_length = 0
        for c in s:
            if c.isalpha():
                decoded_length += 1
            if c.isdigit():
                decoded_length *= int(c)

        # now iterate in reverse and reduce length till we reach k
        for c in reversed(s):
            k %= decoded_length
            
            if k == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                decoded_length /= int(c)
            else:
                decoded_length -= 1