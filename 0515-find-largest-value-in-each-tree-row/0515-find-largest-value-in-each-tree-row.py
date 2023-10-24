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
        queue = deque([root])
        while queue:
            cur_length = len(queue)
            maxval = float('-inf')
            for _ in range(cur_length):
                node = queue.popleft()
                maxval = max(maxval, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(maxval)

        return res