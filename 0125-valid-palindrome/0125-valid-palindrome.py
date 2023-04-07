class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str = ""
        for c in s:
            if c.isalnum():
                str += c.lower()
        
        return str == str[::-1]
        
        