# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast slow pointer to find out 2 halves
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse links from slow.next till end
        prev, cur = None, slow.next
        
        # cut off link between first and second half
        slow.next = None
        
        while cur:
            parent = cur.next
            cur.next = prev
            prev = cur
            cur = parent
        # now prev contains end of linkedlist
        
        # merge two halves
        start, end = head, prev
        while end:
            # start points to end
            startTemp, endTemp = start.next, end.next
            start.next = end
            end.next = startTemp
            start, end = startTemp, endTemp
        
        return head