class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Calculate the decoded string's length until it's at least k.
        decoded_length = 0
        i = 0  # Use a pointer to track where we stop in the string.
        while decoded_length < k:
            if s[i].isalpha():
                decoded_length += 1
            elif s[i].isdigit():
                decoded_length *= int(s[i])
            i += 1

        # Iterate in reverse using the subset of the string we've considered,
        # and reduce length till we reach k.
        for c in reversed(s[:i]):
            k %= decoded_length
            
            if k == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                decoded_length /= int(c)
            else:
                decoded_length -= 1