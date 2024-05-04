# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map = {num: i for i, num in enumerate(inorder)}
        
        def dfs(inorder, postorder):
        
            if not inorder or not postorder:
                return None
            
            root = TreeNode(postorder[-1])
            mid = map[root.val]

            root.left = self.buildTree(inorder[:mid], postorder[:mid])
            root.right = self.buildTree(inorder[mid + 1:], postorder[mid:len(postorder) - 1])

            return root
        
        return dfs(inorder, postorder)