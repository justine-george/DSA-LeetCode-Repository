# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [(root, None)]
        visited = set()
        while stack:
            node, parent = stack.pop()

            if node:
                # Check if node's right child is in visited set
                if node.right and node.right.val in visited:
                    # if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                    continue
                
                visited.add(node.val)

                # Push left child first to the stack (postorder: right-left-root)
                stack.append((node.left, node))
                stack.append((node.right, node))

        return root