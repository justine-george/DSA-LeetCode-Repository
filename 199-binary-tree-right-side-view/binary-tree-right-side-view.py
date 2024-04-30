# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs with depth tracking, keep a dict with depth: value mapping, and update it. return this dict.values in the end.

        depth_val = {}

        def dfs(root, depth):
            if not root:
                return
            
            depth_val[depth] = root.val
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return depth_val.values()

        
        
        # do a level order traversal, and take the last element everytime

        queue = deque([root]) if root else None
        rightside_vals = []

        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rightside_vals.append(row[-1])

        return rightside_vals