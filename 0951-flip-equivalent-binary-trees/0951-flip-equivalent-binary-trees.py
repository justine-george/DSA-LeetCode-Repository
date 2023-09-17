# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # return True if both are null, else return False
        if not root1 or not root2:
            return not root1 and not root2
        
        if root1.val != root2.val:
            return False
        
        # check flip equivalency recursively
        # if both trees are equiv, return True
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        
        # if both trees are flipEquiv, return True else False
        return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)