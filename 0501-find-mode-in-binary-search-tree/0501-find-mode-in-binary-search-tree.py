# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        map = defaultdict(int)

        def traverse(root):
            map[root.val] += 1
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(root)

        mode_val = max(map.values())
        res = []
        for key in map:
            if map[key] == mode_val:
                res.append(key)

        return res
