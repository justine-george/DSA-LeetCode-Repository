# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        recognize the tree is a binary search tree.

        start traversing from root

            if both p and q lies on the left side, traverse left
            if both p and q lies on the right side, traverse right

            2 cases when current node is the lca:
            - if p lies on the left and q on the right or viceversa.
            - if p or q equals current node.
                return current node

        '''

        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur