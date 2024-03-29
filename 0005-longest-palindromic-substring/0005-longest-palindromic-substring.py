class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_index, r_index = 0, 0
        max_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    l_index, r_index = l, r
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    l_index, r_index = l, r
                l -= 1
                r += 1

        
        return s[l_index: r_index + 1]
            
