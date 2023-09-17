# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode()]} # map n to list of Full Binary Tree
        
        # return the list of Full binary trees with n nodes
        def backtrack(n):
            if n % 2 == 0:
                return []
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(1, n, 2): # 1 to n - 1, step 2 since even n means no FBT
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)
                
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            
            dp[n] = res
            return res
        
        return backtrack(n)