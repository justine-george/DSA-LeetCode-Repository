# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        # initialize stack  -in order traversal
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        # return the top of the stack
        res = self.stack.pop()

        # add the next
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.val

    def hasNext(self) -> bool:
        # if stack has value, then next exists
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()