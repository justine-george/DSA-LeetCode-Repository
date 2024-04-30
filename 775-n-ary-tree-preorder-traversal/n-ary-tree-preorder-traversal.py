"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []

        def preorder_dfs(root):
            res.append(root.val)
            for child in root.children:
                if child:
                    preorder_dfs(child)

        preorder_dfs(root)
        return res