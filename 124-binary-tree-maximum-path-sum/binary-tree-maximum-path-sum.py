# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val


        def maxpathsum_without_split(node):
            nonlocal res

            if not node:
                return 0

            left_maxpathsum_without_split = max(maxpathsum_without_split(node.left), 0)
            right_maxpathsum_without_split = max(maxpathsum_without_split(node.right), 0)

            # calculate maxpathsum_with_split and update res
            res = max(res, left_maxpathsum_without_split + node.val + right_maxpathsum_without_split)

            return node.val + max(left_maxpathsum_without_split, right_maxpathsum_without_split)
        

        maxpathsum_without_split(root)
        return res