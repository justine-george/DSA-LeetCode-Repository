# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        '''
        alternate approach: recursive preorder-traversal, with valid ranges
        dfs(root, left, right)
        '''

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))



        '''
        observation: inorder traversal (left, root, right) of a BST is always a strictly-increasing array.
        '''
        # prev_node = None

        # # Inorder traversal - recursive
        # def inorder(node):
        #     nonlocal prev_node
            
        #     if not node:
        #         return True
            
        #     # left
        #     if not inorder(node.left):
        #         return False

        #     # current
        #     if prev_node and prev_node.val >= node.val:
        #         return False
        #     prev_node = node

        #     # right
        #     if not inorder(node.right):
        #         return False

        #     return True

        # return inorder(root)

        # st = []
        # node = root
        # prev_node = None
        # while st or node:
        #     # reach leftmost node
        #     while node:
        #         st.append(node)
        #         node = node.left

        #     node = st.pop()
            
        #     if prev_node and prev_node.val >= node.val:
        #         return False
        #     prev_node = node

        #     node = node.right

        # return True