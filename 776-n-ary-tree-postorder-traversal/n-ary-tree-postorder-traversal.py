"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []

        def dfs(root):
            for child in root.children:
                if child:
                    dfs(child)
            
            res.append(root.val)
        
        dfs(root)
        return res


        # '''
        # iterative dfs using a stack

        # append children, then root.
        # '''

        # stack = [root] if root else None
        # res = []
        # while stack:
        #     node = stack.pop()

        #     if node.children:
        #         for child in node.children:
        #             stack.append(child)

        #     res.append(node.val)

        # return res[::-1]