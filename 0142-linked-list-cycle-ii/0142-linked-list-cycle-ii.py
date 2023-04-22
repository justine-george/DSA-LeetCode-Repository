# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Detects the start node of a cycle in a linked list using Floyd's Cycle Detection algorithm.
        
        Args:
        head: A node representing the head of the linked list.
        
        Returns:
        If a cycle exists in the linked list, returns the node at which the cycle starts.
        Otherwise, returns None.
        
        Time Complexity:
        The time complexity of the algorithm is O(n), where n is the number of nodes in the linked list.

        Space Complexity:
        The space complexity of the algorithm is O(1), as only constant space is used.
        '''
        
        # floyd's cycle detection - find out start of the cycle in 2 phases
        # T: O(n), S: O(1)
        
        # If there are no nodes or only one node, then no cycle
        if head is None or head.next is None:
            return None
        
        # 1. find out the collision point
        # Initialize slow and fast pointers to the head
        slow, fast = head, head
        # Move slow pointer one step and fast pointer two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast pointers meet, a cycle is detected
            if slow == fast:
                # 2. find out the start of cycle using a second slow pointer
                # Move slow2 pointer from the head, while slow pointer continues from the meeting point
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                # When slow and slow2 pointers meet, it's the start of the cycle
                return slow
        
        # If no cycle detected, return None
        return None