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
#         # T: O(n), S: O(1) - keep cloned nodes right next to original
#         if not head:
#             return head
        
#         cur = head
#         while cur:
#             copy = Node(cur.val)
#             # insert new node right next to the original
#             # a,b,c => a,a',b,b',c,c'
#             copy.next = cur.next
#             cur.next = copy
#             cur = copy.next
        
#         cur = head
#         while cur:
#             # point randoms
#             cur.next.random = cur.random.next if cur.random else None
#             cur = cur.next.next
        
#         # unwrap a,a',b,b',c,c' => a,b,c and a',b',c'
#         oldlist = head
#         newlist = head.next
#         headNew = head.next
#         while oldlist:
#             oldlist.next = oldlist.next.next
#             newlist.next = newlist.next.next if newlist.next else None
#             oldlist = oldlist.next
#             newlist = newlist.next
    
#         return headNew
    
    
    
        # T: O(n), S: O(n)
        # iteration
        oldToCopy = {None: None}
        
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
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
    
    
    
#         # T: O(n), S: O(n)
#         # recursion
#         oldToCopy = {}
        
#         def dfs(node):
#             if node == None:
#                 return None
            
#             if node in oldToCopy:
#                 return oldToCopy[node]
            
#             newNode = Node(node.val)
#             oldToCopy[node] = newNode
            
#             newNode.next = dfs(node.next)
#             newNode.random = dfs(node.random)
            
#             return newNode
        
#         return dfs(head)