# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(start):
            prev, curr = None, start
            while curr:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            
            return prev
        
        def getSecondHalfHead(start):
            slow, fast = start, start.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            res = slow.next
            slow.next = None
            return res
        
        if not head.next:
            return True
        
        # get reversed secondhalf head
        revHead = reverse(getSecondHalfHead(head))
        
        # compare each node to check equivalency
        curr, revCurr = head, revHead
        while revCurr:
            if curr.val != revCurr.val:
                return False
            curr = curr.next
            revCurr = revCurr.next
        
        return True