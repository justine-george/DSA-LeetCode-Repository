# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # def dfs(node, max_so_far):
        #     if not node:
        #         return 0
            
        #     count = 0
        #     if node.val >= max_so_far:
        #         max_so_far = node.val
        #         count += 1

        #     count += dfs(node.left, max_so_far)
        #     count += dfs(node.right, max_so_far)

        #     return count
        
        # return dfs(root, float('-inf'))

        st = [(root, float('-inf'))] if root else None
        count = 0
        while st:
            node, max_so_far = st.pop()

            if not node:
                continue

            if node.val >= max_so_far:
                max_so_far = node.val
                count += 1
            
            st.append((node.left, max_so_far))
            st.append((node.right, max_so_far))
        
        return count