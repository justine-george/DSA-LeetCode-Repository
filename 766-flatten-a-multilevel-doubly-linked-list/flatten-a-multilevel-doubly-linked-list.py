"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        if not head:
            return None

        dummy = Node(0)
        self.flattenDFS(dummy, head)

        dummy.next.prev = None
        return dummy.next
        '''
        if not head:
            return None

        dummy = Node(0)
        prev = dummy
        stack = [head]
        while stack:
            cur = stack.pop()

            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
            
            prev.next = cur
            cur.prev = prev
            cur.child = None
            prev = cur
        
        dummy.next.prev = None
        return head
    
    '''
    def flattenDFS(self, prev: 'Node', cur: 'Node') -> 'Node':
        if not cur:
            return prev
        
        tempNext = cur.next
        child = cur.child

        prev.next = cur
        cur.prev = prev

        tail = self.flattenDFS(cur, child)
        cur.child = None
        return self.flattenDFS(tail, tempNext)
    '''