# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode()
        cur = dummy
        carry  = 0
        
        # carry is for the case when one last carry remains
        while l1 or l2 or carry :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            carry, digit = divmod(v1 + v2 + carry, 10) # quotient, remainder
            cur.next = ListNode(digit)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next