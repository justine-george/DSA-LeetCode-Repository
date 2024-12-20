# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        '''
        # BFS
        if not root:
            return None
        
        # (node, parent)
        q = deque([(root, None)])
        visited = set()
        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()
                
                if node.right and node.right.val in visited:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root
                
                visited.add(node.val)

                # Push right child first to the queue, so that right is processed first
                if node.right:
                    q.append((node.right, node))
                if node.left:
                    q.append((node.left, node))
        '''

        # DFS
        if not root:
            return None

        stack = [(root, None)]
        visited = set()
        while stack:
            node, parent = stack.pop()

            if node.right and node.right.val in visited:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            
            visited.add(node.val)

            # Push left child first to the stack (since we should process right first)
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))