# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0] # global variable
        
        def longestPath(node):
            if not node:
                return 0
                      
            leftHeight = longestPath(node.left)
            rightHeight = longestPath(node.right)

            # nonlocal dia
            # either use nonlocal or use an array of size 1
            dia[0] = max(dia[0], leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1
        
        longestPath(root)
        return dia[0]