# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root is None:
        #     return False

        # leftoverSum = targetSum - root.val
        
        # if root.left is None and root.right is None and leftoverSum == 0:
        #     return True
        
        # return self.hasPathSum(root.left, leftoverSum) or \
        #     self.hasPathSum(root.right, leftoverSum)

        if not root:
            return False

        stack = [(root, targetSum)]
        while stack:
            cur, target = stack.pop()
            # if cur:
            residualSum = target - cur.val                
            if not cur.left and not cur.right and residualSum == 0:
                return True

            if cur.right:
                stack.append((cur.right, residualSum))
            if cur.left:
                stack.append((cur.left, residualSum))

        return False