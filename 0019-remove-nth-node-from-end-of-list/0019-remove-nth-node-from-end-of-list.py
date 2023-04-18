# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # before
        # [dummy->1 2 3 4 5->null]
        #  l          r
    
        # after
        # [dummy->1 2 3 4 5->null]
        #             l      r
        
        # using a dummy at the beginning is the key!
        # l = dummy
        # r = nth value from start
        dummy = ListNode(0, head)
        l, r = dummy, head
        i = 0
        while i != n and r:
            r = r.next
            i += 1
        
        # now shift both pointers till r is null
        while r:
            l, r = l.next, r.next
        
        # now l.next points to the nth node from the end!
        l.next = l.next.next
        return dummy.next