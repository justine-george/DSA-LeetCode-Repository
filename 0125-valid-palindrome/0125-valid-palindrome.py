class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # trivial solution, S: O(n)
#         str = ""
#         for c in s:
#             if c.isalnum():
#                 str += c.lower()
#         return str == str[::-1]
    
        # Two pointers - S: O(1)
        def isalphanum(c):
            return ((ord('0') <= ord(c) <= ord('9')) or 
                    (ord('A') <= ord(c) <= ord('Z')) or 
                    (ord('a') <= ord(c) <= ord('z')))
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while not isalphanum(s[l]) and l < r:
                l += 1
            while not isalphanum(s[r]) and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
        