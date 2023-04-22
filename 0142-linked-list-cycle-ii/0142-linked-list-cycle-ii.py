# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # floyd's cycle detection - find out start of the cycle in 2 phases
        
        if head is None or head.next is None:
            return None
        
        # 1. find out the collision point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if slow != fast:
            return None
        
        # 2. find out the start of cycle using a second slow pointer
        slow2 = head
        while True:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
            