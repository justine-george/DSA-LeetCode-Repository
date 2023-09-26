class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from each character and go outwards
        # consider both odd and even length palindromes
        # O(n**2)
        resLength, res_start_index, res_end_index = 0, 0, 0

        for i in range(len(s)):
            # odd
            resLength, res_start_index, res_end_index = self.checkPalindrome(i, i, s, resLength, res_start_index, res_end_index)

            # even
            resLength, res_start_index, res_end_index = self.checkPalindrome(i, i + 1, s, resLength, res_start_index, res_end_index)
        
        return s[res_start_index: res_end_index + 1]

    def checkPalindrome(self, l, r, s, resLength, res_start_index, res_end_index):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLength:
                resLength = r - l + 1
                res_start_index = l
                res_end_index = r
            l -= 1
            r += 1
        return (resLength, res_start_index, res_end_index)