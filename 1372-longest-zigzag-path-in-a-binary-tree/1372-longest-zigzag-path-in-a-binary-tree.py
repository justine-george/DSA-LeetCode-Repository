# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def zigzag(node, direction, depth):
            if not node:
                return depth
            
            if direction == 'l':
                return max(zigzag(node.right, 'r', depth + 1), zigzag(node.left, 'l', 0))
            else:
                return max(zigzag(node.left, 'l', depth + 1), zigzag(node.right, 'r', 0))
            
        return max(zigzag(root.left, 'l', 0), zigzag(root.right, 'r', 0))