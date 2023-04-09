# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        leftSame = self.isSubtree(root.left, subRoot)
        rightSame = self.isSubtree(root.right, subRoot)
        
        return leftSame or rightSame