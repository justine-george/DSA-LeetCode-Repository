class Solution:
    def climbStairs(self, n: int) -> int:
        
        # T: O(n), S: O(1)
        last = 1
        secondLast = 1
        for i in range(n - 2, -1, -1):
            cur = secondLast + last
            last = secondLast
            secondLast = cur
        return secondLast
    
    
       
        