class Solution:
    def countSubstrings(self, s: str) -> int:
        # start from each character and go outwards
        # consider both odd and even length palindromes
        # O(n**2)
        res = 0

        for i in range(len(s)):
            # odd
            res += self.countPalindrome(i, i, s)

            # even
            res += self.countPalindrome(i, i + 1, s)
        
        return res

    def countPalindrome(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res