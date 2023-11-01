# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        map, max_freq = self.getMaxFreq(root)
        
        res = []
        for key in map:
            if map[key] == max_freq:
                res.append(key)
        return res

    def getMaxFreq(self, root):
        map = defaultdict(int)
        queue = deque([root])
        depth = 0
        while queue:
            queue_len = len(queue)
            print(f"Level: {depth}")
            for i in range(queue_len):
                node = queue.popleft()
                map[node.val] += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        max_freq = max(map.values())
        return map, max_freq