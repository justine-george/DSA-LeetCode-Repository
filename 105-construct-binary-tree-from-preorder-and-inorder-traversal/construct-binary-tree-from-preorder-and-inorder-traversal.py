# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        observation:
            preorder[0] is the root
            split inorder at this 'root', find len numbers left and right
            preorder[1:] -> leftnumbers: left tree, remaining rightnumbers: righttree

        '''

        map = {num: i for i, num in enumerate(inorder)}

        def build(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = map[preorder[0]] # saving O(n) into O(1)
            root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

            return root

        return build(preorder, inorder)