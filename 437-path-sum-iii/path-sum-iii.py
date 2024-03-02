# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.counter = 0
        self.targetSum = targetSum
        self.dfs(root, 0, {0: 1})
        return self.counter

    def dfs(self, node, curSum, prevSums):
        if not node:
            return
        
        curSum += node.val
        self.counter += prevSums.get(curSum - self.targetSum, 0)

        # update map
        prevSums[curSum] = prevSums.get(curSum, 0) + 1

        # traverse left and right
        self.dfs(node.left, curSum, prevSums)
        self.dfs(node.right, curSum, prevSums)

        # backtrack
        prevSums[curSum] -= 1
        if prevSums[curSum] == 0:
            del prevSums[curSum]

        # if not root:
        #     return 0

        # stack = [(root, 0, {0: 1})]
        # counter = 0
        # while stack:
        #     currentNode, curSum, prevSums = stack.pop()
        #     if not currentNode:
        #         continue

        #     curSum += currentNode.val
        #     counter += prevSums.get(curSum - targetSum, 0)

        #     newSums = prevSums.copy()
        #     newSums[curSum] = newSums.get(curSum, 0) + 1

        #     stack.append((currentNode.right, curSum, newSums))
        #     stack.append((currentNode.left, curSum, newSums))

        # return counter