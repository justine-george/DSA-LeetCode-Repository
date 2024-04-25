# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def getMaxDepth(root):
            if not root: return 0

            nonlocal diameter
            leftMaxDepth = getMaxDepth(root.left)
            rightMaxDepth = getMaxDepth(root.right)

            diameter = max(diameter, leftMaxDepth + rightMaxDepth)

            return max(leftMaxDepth, rightMaxDepth) + 1
        
        getMaxDepth(root)
        return diameter