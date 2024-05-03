# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        '''
        observation: inorder traversal (left, root, right) of a BST is always a strictly-increasing array.
        '''

        prev_node = None
        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            nonlocal prev_node
            if prev_node and prev_node.val >= node.val:
                return False
            prev_node = node
            if not inorder(node.right):
                return False

            return True

        return inorder(root)


        # st = [(root)] if root else None
        # prev_node = None
        # while st:
        #     node = st.pop()

        #     if not node:
        #         continue

        #     st.append(node.left)

        #     if prev_node and prev_node.val >= node.val:
        #         return False
            
        #     st.append(node.right)

        #     prev_node = node

        # return True