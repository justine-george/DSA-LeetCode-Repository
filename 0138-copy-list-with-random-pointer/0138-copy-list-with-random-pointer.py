"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}
        
        # first create the deep copies, we're not pointing yet
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy # map old to new node
            cur = cur.next
        
        # now add the connections
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy.get(cur.next, None)
            copy.random = oldToCopy.get(cur.random, None)
            cur = cur.next
        
        return oldToCopy.get(head, None)