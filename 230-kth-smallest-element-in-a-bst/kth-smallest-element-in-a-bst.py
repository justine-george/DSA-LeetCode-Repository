# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_val = -1
        count = 1

        def inorder(node):
            nonlocal k_val, count
            
            if not node or k_val != -1:
                return
            
            inorder(node.left)

            if k_val == -1 and count == k:
                k_val = node.val
                return
            
            count += 1
            inorder(node.right)

        inorder(root)
        return k_val