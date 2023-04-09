# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
            
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        q = collections.deque([root]) if root else None
        levelCount = 0
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levelCount += 1
                
        return levelCount