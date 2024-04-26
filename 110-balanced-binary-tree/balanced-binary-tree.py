# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root:
                return (0, True)

            leftDepth, leftPossible = getDepth(root.left)
            rightDepth, rightPossible = getDepth(root.right)

            return (max(leftDepth, rightDepth) + 1, (abs(rightDepth - leftDepth) <= 1) and leftPossible and rightPossible)
        
        return getDepth(root)[1]