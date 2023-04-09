# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dia = 0
        def longestPath(node):
            if not node:
                return 0
                      
            leftHeight = longestPath(node.left)
            rightHeight = longestPath(node.right)

            nonlocal dia
            dia = max(dia, leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1
        
        longestPath(root)
        return dia