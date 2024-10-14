# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getDepth(node):
            if not node:
                return (True, 0)
        
            leftPossible, leftDepth = getDepth(node.left)
            rightPossible, rightDepth = getDepth(node.right)

            return (leftPossible and rightPossible and abs(leftDepth - rightDepth) <= 1, 1 + max(leftDepth, rightDepth))
        
        return getDepth(root)[0]