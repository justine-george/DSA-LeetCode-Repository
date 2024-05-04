# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxval = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxval

    # return max path sum without splitting
    def dfs(self, node):
        if not node:
            return 0
        
        leftmax = max(self.dfs(node.left), 0)
        rightmax = max(self.dfs(node.right), 0)

        # calculate max path sum with splitting
        self.maxval = max(self.maxval, leftmax + node.val + rightmax)

        return node.val + max(leftmax, rightmax)