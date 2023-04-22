# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # floyd's cycle detection - find out start of the cycle in 2 phases
        
        # if there is no nodes or only one node, then no cycle
        if head is None or head.next is None:
            return None
        
        # 1. find out the collision point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 2. find out the start of cycle using a second slow pointer
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                # When slow and slow2 pointers meet, it's the start of the cycle
                return slow
        
        # if no cycle is detected
        return None