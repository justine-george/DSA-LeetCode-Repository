# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(node, level=0):
            if not node:
                return 0

            return max(1 + findDepth(node.left), 1 + findDepth(node.right))
        
        return findDepth(root)