# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def revOdd(l, r, level=1):
            if not l:
                return
            
            if level % 2 != 0:
                # swap values instead of nodes itself
                l.val, r.val = r.val, l.val
            
            revOdd(l.left, r.right, level + 1)
            revOdd(l.right, r.left, level + 1)
        
        revOdd(root.left, root.right)
        return root