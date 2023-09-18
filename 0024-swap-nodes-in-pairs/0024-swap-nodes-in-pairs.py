# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode()
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr and curr.next:
            nextGroup = curr.next.next
            next = curr.next
            next.next = curr
            prev.next = next
            curr.next = nextGroup
            
            prev = curr
            curr = nextGroup
        
        return dummy.next
            
            
            
        # dummy-1-2-3-4
        # dummy-1-2-1-2.. 3-4
        # dummy-2-1-2.. 3-4
        # dummy-2-1-3-4
        