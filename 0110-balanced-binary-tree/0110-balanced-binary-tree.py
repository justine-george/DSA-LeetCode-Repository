# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True
        def getHeight(node):
            nonlocal isBalanced
            if not node:
                return 0
            
            leftH = getHeight(node.left)
            rightH = getHeight(node.right)
            
            if (abs(leftH - rightH) > 1):
                isBalanced = False
            return 1 + max(leftH, rightH)
        
        getHeight(root)
        return isBalanced
        