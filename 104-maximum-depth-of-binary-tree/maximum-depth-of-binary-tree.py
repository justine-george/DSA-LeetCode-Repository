# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



        #dfs
        stack = [(root, 1)] if root else None
        maxdepth = 0
        while stack:
            cur, depth = stack.pop()
            maxdepth = max(maxdepth, depth)
            if cur.left:
                stack.append((cur.left, depth + 1))
            if cur.right:
                stack.append((cur.right, depth + 1))
        return maxdepth
