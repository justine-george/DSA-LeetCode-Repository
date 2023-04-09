# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]
            
            leftH = dfs(node.left)\
            # if left side is unbalanced, no need to traverse right
            if not leftH[0]:
                return [False, -1]
            
            rightH = dfs(node.right)
            
            isBalanced = (leftH[0] and 
                          rightH[0] and 
                          abs(leftH[1] - rightH[1]) <= 1)
    
            return [isBalanced, 1 + max(leftH[1], rightH[1])]
        
        return dfs(root)[0]