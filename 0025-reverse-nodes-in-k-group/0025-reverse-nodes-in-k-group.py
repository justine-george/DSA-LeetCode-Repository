# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            prevFirstNode = groupPrev.next
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # reverse group
            # two pointers
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            
            
            groupPrev.next = kth
            prevFirstNode.next = groupNext
            groupPrev = prevFirstNode
        
        return dummy.next
            
        
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr