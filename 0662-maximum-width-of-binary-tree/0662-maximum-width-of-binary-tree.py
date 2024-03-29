# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS solution
        # T: O(n), S: O(n)
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
    
        
#         # DFS solution
#         # T: O(n), S: O(n)
#         if not root:
#             return 0

#         # save first visit of a node in a particular depth
#         firstNodeDepth = {}
        
#         maxWidth = 0
#         def dfs(node, depth, colIndex):
#             nonlocal maxWidth
#             if not node:
#                 return
            
#             if depth not in firstNodeDepth:
#                 firstNodeDepth[depth] = colIndex
            
#             maxWidth = max(maxWidth, colIndex - firstNodeDepth[depth] + 1)
            
#             dfs(node.left, depth + 1, 2 * colIndex)
#             dfs(node.right, depth + 1, 2 * colIndex + 1)
            
#             return maxWidth
        
#         return dfs(root, 0, 0)