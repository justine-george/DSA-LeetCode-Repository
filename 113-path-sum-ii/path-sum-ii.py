# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.res = []
        self.dfs(root, [], targetSum)
        return self.res

    def dfs(self, node, curPath, remSum):
        newPath = curPath + [node.val]
        newRemSum = remSum - node.val

        if not node.left and not node.right and newRemSum == 0:
            self.res.append(newPath)
            return
            
        if node.right:
            self.dfs(node.right, newPath, newRemSum)
        if node.left:
            self.dfs(node.left, newPath, newRemSum)

        # res = []
        # if not root:
        #     return res
        
        # stack = [(root, [], targetSum)]
        # while stack:
        #     cur, path, remSum = stack.pop()
        #     if cur:
        #         path.append(cur.val)
        #         newRemSum = remSum - cur.val
        #         if not cur.left and not cur.right and newRemSum == 0:
        #             res.append(path)
        #             continue
        #         if cur.right:
        #             stack.append((cur.right, path[:], newRemSum))
        #         if cur.left:
        #             stack.append((cur.left, path[:], newRemSum))
        # return res

        # target = 22

        # [
        #     22, 5, []
        # ]

        # 22, 5, []
        
        # target - sum(list) = 17



