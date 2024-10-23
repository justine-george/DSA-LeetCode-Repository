"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # clone kids
        # clone this node, and add kids to children
        # return new node

        newChildren = []
        for child in root.children:
            newChildren.append(self.cloneTree(child))
        return Node(root.val, newChildren)