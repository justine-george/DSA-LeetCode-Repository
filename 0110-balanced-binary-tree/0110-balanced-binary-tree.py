# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(node):
            if not node:
                return [True, 0]
            
            leftH, rightH = getHeight(node.left), getHeight(node.right)
            
            isBalanced = (leftH[0] and 
                          rightH[0] and 
                          abs(leftH[1] - rightH[1]) <= 1)
    
            return [isBalanced, 1 + max(leftH[1], rightH[1])]
        
        return getHeight(root)[0]