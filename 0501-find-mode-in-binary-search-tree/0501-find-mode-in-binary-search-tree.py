# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        map = defaultdict(int)
        self.traverse(root, map)
        mode_val = max(map.values())
        
        res = []
        for key in map:
            if map[key] == mode_val:
                res.append(key)
        return res

    def traverse(self, root, map):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                map[node.val] += 1
                stack.append(node.left)
                stack.append(node.right)
