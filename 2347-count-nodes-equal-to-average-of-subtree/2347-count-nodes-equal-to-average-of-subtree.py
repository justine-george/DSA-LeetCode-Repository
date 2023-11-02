# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def avg(node):
            nonlocal res

            # leaf node
            if not node:
                return 0, 0
            
            totalL = totalR = countL = countR = 0
            if node.left:
                countL, totalL = avg(node.left)
            if node.right:
                countR, totalR = avg(node.right)

            totalCount = 1 + countL + countR
            totalSum = totalL+ totalR + node.val
            if totalSum // totalCount == node.val:
                res += 1
            
            print(f"Node: {node.val}, totalCount: {totalCount}, totalSum: {totalSum}")
            
            return totalCount, totalSum
            
        level, total = avg(root)
        return res
