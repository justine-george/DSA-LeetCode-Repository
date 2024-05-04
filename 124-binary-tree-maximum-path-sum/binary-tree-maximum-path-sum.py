# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = float('-inf')

        # return max path sum without splitting
        def dfs(node):
            nonlocal maxval

            if not node:
                return 0
            
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)

            # calculate max path sum with splitting
            maxval = max(maxval, leftmax + node.val + rightmax)

            return node.val + max(leftmax, rightmax)


        dfs(root)
        return maxval