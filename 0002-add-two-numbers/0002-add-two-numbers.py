# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        carry = 0
        temp1, temp2 = l1, l2
        res = []
        while temp1 and temp2:
            node = ListNode(temp1.val + temp2.val + carry)
            carry = 0
            if node.val > 9:
                node.val = node.val % 10
                carry = 1
                
            res.append(node)
            temp1 = temp1.next
            temp2 = temp2.next
        
        while temp1:
            node = ListNode(temp1.val + carry)
            carry = 0
            if node.val > 9:
                node.val = node.val % 10
                carry = 1
            
            res.append(node)
            temp1 = temp1.next
        
        while temp2:
            node = ListNode(temp2.val + carry)
            carry = 0
            if node.val > 9:
                node.val = node.val % 10
                carry = 1
            
            res.append(node)
            temp2 = temp2.next
        
        if carry == 1:
            res.append(ListNode(1))
        
        # now connect res nodes
        head = res[0]
        for i in range(len(res) - 2, -1, -1):
            res[i].next = res[i + 1]
            
        return head