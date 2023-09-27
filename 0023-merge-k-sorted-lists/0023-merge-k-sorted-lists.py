# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeTwoList(l1, l2))
                # if i + 1 < len(lists):
                #     mergedList.append(self.mergeTwoList(lists[i], lists[i + 1]))
                # else:
                #     mergedList.append(self.mergeTwoList(lists[i], None))
            lists = mergedList

        return lists[0]
    
    def mergeTwoList(self, l1, l2):
        res = ListNode()
        cur = res
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2
        
        return res.next