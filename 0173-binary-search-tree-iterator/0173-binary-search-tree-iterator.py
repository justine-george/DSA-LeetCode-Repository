# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        # add root to the stack
        self.fill_stack(root)

    def next(self) -> int:
        # return the top of the stack
        res = self.stack.pop()
        
        # add res's right child to the stack
        self.fill_stack(res.right)

        return res.val

    def hasNext(self) -> bool:
        # if stack has value, then next exists
        return len(self.stack) != 0

    # adds node to stack and all its left child, till None
    def fill_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()