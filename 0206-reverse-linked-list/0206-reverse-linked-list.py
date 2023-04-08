# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # T: O(n), S: O(1)
        # cur, prev = head, None
        # while cur:
        #     parent = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = parent
        # return prev
    
        # T: O(n), S:O(n)
        # explanation here: https://www.youtube.com/watch?v=S92RuTtt9EE
        # if empty linkedlist is passed - validation
        if not head:
            return head
        
        # proper base case
        if not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        
        return newHead
        

