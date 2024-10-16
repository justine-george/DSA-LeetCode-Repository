# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        dummy = TreeNode(0)
        prev = dummy
        stack = [root]

        while stack:
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
            prev.right = cur
            prev.left = None
            prev = cur
        
        root = dummy.right