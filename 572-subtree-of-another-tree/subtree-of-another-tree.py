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
        string_root = self.traverse_tree(root)
        string_subroot = self.traverse_tree(subRoot)
        # if string_subroot in string_root:
        #     return True
        # return True if string_subroot in string_root else False
        return string_subroot in string_root


    def traverse_tree(self, node):
        if node:
            return f"#{node.val} {self.traverse_tree(node.left)} {self.traverse_tree(node.right)}"
        return 'n'
    
    