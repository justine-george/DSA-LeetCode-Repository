# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # recursive dfs
#         # T: O(n), S: O(n)
#         # if balanced tree, then S: O(logn)
#         if not root:
#             return 0
            
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#         # iterative bfs
#         # T: O(n), S: O(n)
#         # if it is a skewed binary tree, max queue size would be just 1
#         q = collections.deque([root]) if root else None
#         levelCount = 0
        
#         while q:
#             for i in range(len(q)): # pop all nodes in this level
#                 cur = q.popleft()
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#             levelCount += 1
                
#         return levelCount
        
        # iterative dfs
        # T: O(n), S: O(n)
        # st = [[root, 1]] if root else None
        st = collections.deque([[root, 1]]) if root else None
        maxLevel = 0
        while st:
            curNode, curLevel = st.pop()
            maxLevel = max(maxLevel, curLevel)
            if curNode.left:
                st.append([curNode.left, curLevel + 1])
            if curNode.right:
                st.append([curNode.right, curLevel + 1])
        return maxLevel