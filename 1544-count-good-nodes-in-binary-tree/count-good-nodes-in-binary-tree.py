# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        iterative/recursive dfs

        for each dfs(root, max_so_far) iteration:
            if node.val >= max_so_far, increment count and update max_so_far
            increment counts from dfs(left, newmax) and dfs(right, newmax)
            return count

        return dfs(root, initial = float('-inf'))
        '''

        def dfs(root, max_so_far):
            if not root:
                return 0
            
            count = 0
            if root.val >= max_so_far:
                max_so_far = root.val
                count += 1
            
            count += dfs(root.left, max_so_far)
            count += dfs(root.right, max_so_far)
            return count
        
        return dfs(root, float('-inf'))