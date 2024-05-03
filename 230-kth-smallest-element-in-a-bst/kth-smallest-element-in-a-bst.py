# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth_val = -1
        # count = 1

        # def inorder(node):
        #     nonlocal kth_val, count

        #     if not node or kth_val != -1:
        #         return
            
        #     inorder(node.left)

        #     if kth_val == -1 and count == k:
        #         kth_val = node.val
        #         return
        #     count += 1

        #     inorder(node.right)

        # inorder(root)
        # return kth_val



        # iterative inorder
        st = []
        node = root
        count = 0
        while st or node:
            while node:
                st.append(node)
                node = node.left
            
            node = st.pop()
            count += 1
            if count == k:
                return node.val
            
            node = node.right

        return -1