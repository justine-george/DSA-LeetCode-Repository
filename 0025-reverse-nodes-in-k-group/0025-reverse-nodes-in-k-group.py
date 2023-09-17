# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        while True:
            firstNode = groupPrev.next
            kth = getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # reverse the k size group
            prev, curr = groupNext, firstNode
            while curr != groupNext:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            
            groupPrev.next = kth
            firstNode.next = groupNext
            groupPrev = firstNode
                
        
        
        
        return dummy.next