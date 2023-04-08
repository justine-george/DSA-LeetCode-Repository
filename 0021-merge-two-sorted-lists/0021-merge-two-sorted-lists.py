# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        p1, p2 = list1, list2
        res = ListNode(0, None) # dummy node
        newHead = res
        while p1 and p2:
            if p1.val <= p2.val:
                res.next = p1
                res = res.next
                p1 = p1.next
            else:
                res.next = p2
                res = res.next
                p2 = p2.next
        
        while p1:
            res.next = p1
            res = res.next
            p1 = p1.next
        
        while p2:
            res.next = p2
            res = p2
            p2 = p2.next
            
        return newHead.next # next contains the actual head of the new LL