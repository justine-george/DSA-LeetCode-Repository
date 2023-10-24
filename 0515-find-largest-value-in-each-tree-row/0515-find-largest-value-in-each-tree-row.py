# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        cur_level = 0
        queue = deque()
        queue.append((root, cur_level))
        maxval = float('-inf')
        while queue:
            node, level = queue.popleft()
            if level != cur_level:
                res.append(maxval)
                maxval = float('-inf')
                cur_level = level
            
            maxval = max(maxval, node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res.append(maxval)
        return res