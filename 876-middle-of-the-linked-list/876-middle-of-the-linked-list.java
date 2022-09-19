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
    public ListNode middleNode(ListNode head) {
        int size = 1;
        ListNode temp = head;
        while (temp.next != null) {
            temp = temp.next;
            size++;
        }
        
        int mid = size/2 + 1;
        
        temp = head;
        while (mid != 1) {
            temp = temp.next;
            mid--;
        }
        
        return temp;
    }
}