# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        # queue -> [(node, colIndex)] colIndex starting from 0
        q = collections.deque([(root, 0)])
        
        while q:
            levelLength = len(q)
            _, levelHeadIndex = q[0]
            
            # iterate through the current level
            for _ in range(levelLength):
                cur, colIndex = q.popleft()
                if cur.left:
                    q.append((cur.left, 2 * colIndex))
                if cur.right:
                    q.append((cur.right, 2 * colIndex + 1))
            
            maxWidth = max(maxWidth, colIndex - levelHeadIndex + 1)
        
        return maxWidth