class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].lower().isalnum() and l < r:
                l += 1
            while not s[r].lower().isalnum() and l < r:
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True