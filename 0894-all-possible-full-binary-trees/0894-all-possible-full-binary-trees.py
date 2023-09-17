# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        
        def generateFBT(n):
            if n in dp:
                return dp[n]
            
            if n % 2 == 0:
                return []
            
            if n == 0:
                return []
            
            if n == 1:
                return [TreeNode()]
            
            res = []
            for l in range(1, n, 2):
                r = n - 1 - l
                
                leftTrees, rightTrees = generateFBT(l), generateFBT(r)
                for t1, t2 in product(leftTrees, rightTrees):
                    res.append(TreeNode(0, t1, t2))
            
            dp[n] = res
            return res
        
        return generateFBT(n)