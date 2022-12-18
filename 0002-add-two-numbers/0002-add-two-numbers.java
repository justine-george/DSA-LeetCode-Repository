/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode res = new ListNode();
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        ListNode temp3 = res;
        while (temp1 != null && temp2 != null) {
            temp3 = makeNode((temp1.val + temp2.val + carry) % 10, temp3);
            carry = (temp1.val + temp2.val + carry) / 10;
            temp1 = temp1.next;
            temp2 = temp2.next;
            
        }
        while (temp1 != null) {
            temp3 = makeNode((temp1.val + carry) % 10, temp3);
            carry = (temp1.val + carry) / 10;
            temp1 = temp1.next;
        }
        while (temp2 != null) {
            temp3 = makeNode((temp2.val + carry) % 10, temp3);
            carry = (temp2.val + carry) / 10;
            temp2 = temp2.next;
        }
        if (carry == 1) {
            temp3 = makeNode(1, temp3);
        }
        return res.next;
    }
    
    private ListNode makeNode(int val, ListNode temp3) {
        ListNode newVal = new ListNode(val);
        temp3.next = newVal;
        temp3 = newVal;
        return temp3;
    }
}

 


