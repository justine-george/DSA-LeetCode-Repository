# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        l, r = dummy, head
        while k > 1:
            r = r.next
            k -= 1
        
        # r is the kth node from start
        kstart = r
        
        while r:
            l = l.next
            r = r.next
        
        # l is the kth node from end
        kend = l
        
        # swap
        tmp = kstart.val
        kstart.val = kend.val
        kend.val = tmp
        
        return dummy.next