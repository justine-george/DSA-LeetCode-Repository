class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str = ""
        for c in s:
            if c.isalnum():
                str += c.lower()
        
        revStr = str[::-1]
        
        return str == revStr
        
        