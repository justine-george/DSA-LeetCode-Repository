class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = []
        for c in s:
            if c.isalnum():
                l.append(c.lower())
        
        str = "".join(l)
        revStr = str[::-1]
        
        return str == revStr
        
        