# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.isSameTree(root, subRoot):
    #         return True

    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    # def isSameTree(self, node1, node2):
    #     if not node1 and not node2:
    #         return True
    #     if not node1 or not node2 or node1.val != node2.val:
    #         return False
        
    #     return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)

        return self.tree_to_string(subRoot) in self.tree_to_string(root)


    def tree_to_string(self, node):
        if node:
            return f"#{node.val} {self.tree_to_string(node.left)} {self.tree_to_string(node.right)}"
        return 'n'
    
    