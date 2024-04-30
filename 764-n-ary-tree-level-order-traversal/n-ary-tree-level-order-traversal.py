"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        use a deque to iterate over the n-ary tree BFS level by level
            track the current popped element in a list
            add non null children to a deque
            once a level is done, add this list to the result list 

        '''

        queue = deque([root]) if root else None
        levels = []
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)

                if node.children:
                    for childNode in node.children:
                        if childNode:
                            queue.append(childNode)
            levels.append(row)
        
        return levels