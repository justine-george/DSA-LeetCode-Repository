# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # recursive solution - DFS
        # if not root: return

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left

        # return root

        # # iterative solution - DFS
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack.append(node.left)
        #         stack.append(node.right)
        
        # return root

        # iterative solution - BFS
        stack = deque([root])

        while stack:
            node = stack.popleft()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        
        return root