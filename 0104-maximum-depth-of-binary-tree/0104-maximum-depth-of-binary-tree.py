# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # recursive dfs: T: O(n), S: O(n)
#         # if balanced tree, then S: O(logn)
#         if not root:
#             return 0
            
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iterative bfs
        # T: O(n), S: O(n)
        # if it is a skewed binary tree, max queue size would be just 1
        q = collections.deque([root]) if root else None
        levelCount = 0
        
        while q:
            for i in range(len(q)): # pop all nodes in this level
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levelCount += 1
                
        return levelCount