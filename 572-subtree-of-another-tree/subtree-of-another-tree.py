# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right) and node1.val == node2.val
        
        possible_list = []

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                possible_list.append(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        for node in possible_list:
            if isSameTree(node, subRoot):
                return True
        
        return False