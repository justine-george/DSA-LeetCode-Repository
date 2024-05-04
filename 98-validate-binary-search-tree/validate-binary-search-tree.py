# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = []
        node = root
        prev = None
        while st or node:
            while node:
                st.append(node)
                node = node.left
            
            node = st.pop()

            # logic
            if prev and prev.val >= node.val:
                return False
            prev = node

            node = node.right
        
        return True