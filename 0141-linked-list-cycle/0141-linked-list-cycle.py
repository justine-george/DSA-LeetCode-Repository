# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # T: O(n), S: O(n)
        # temp = head
        # visited = set()
        # while temp:
        #     if temp in visited:
        #         return True
        #     visited.add(temp)
        #     temp = temp.next
        # return False
    
    
        # slow-fast pointer T: O(n), S: O(1)
        # if they meet, cycle present!
        slow, fast = head, head
        # break out of this loop if fast reaches end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
            if slow == fast:
                return True
            
        return False
    