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
import java.math.BigInteger;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode res = new ListNode();
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        ListNode temp3 = res;
        
        BigInteger num1 = new BigInteger("0");
        BigInteger num2 = new BigInteger("0");
        BigInteger num3 = new BigInteger("0");
        
        BigInteger zero = new BigInteger("0");
        BigInteger ten = new BigInteger("10");
        
        StringBuilder n1 = new StringBuilder();
        StringBuilder n2 = new StringBuilder();
        
        while(temp1 != null) {
            n1.append(temp1.val);
            temp1 = temp1.next;
        }
        n1 = n1.reverse();
        System.out.println(n1);
        
        while(temp2 != null) {
            n2.append(temp2.val);
            temp2 = temp2.next;
        }
        n2 = n2.reverse();
        System.out.println(n2);
        
        num1 = new BigInteger(n1.toString());
        num2 = new BigInteger(n2.toString());
        
        num3 = num1.add(num2);
        
        System.out.println(num3);
        
        if (num3.equals(zero)) {
            return new ListNode(0);
        }
        
        while(!num3.equals(zero)) {
            ListNode newVal = new ListNode((num3.mod(ten)).intValue());
            temp3.next = newVal;
            temp3 = newVal;
            num3 = num3.divide(ten);
        }
        
//         while (temp1 != null && temp2 != null) {
//             temp3 = makeNode((temp1.val + temp2.val + carry) % 10, temp3);
//             carry = (temp1.val + temp2.val + carry) / 10;
//             temp1 = temp1.next;
//             temp2 = temp2.next;
            
//         }
//         while (temp1 != null) {
//             temp3 = makeNode((temp1.val + carry) % 10, temp3);
//             carry = (temp1.val + carry) / 10;
//             temp1 = temp1.next;
//         }
//         while (temp2 != null) {
//             temp3 = makeNode((temp2.val + carry) % 10, temp3);
//             carry = (temp2.val + carry) / 10;
//             temp2 = temp2.next;
//         }
//         if (carry == 1) {
//             temp3 = makeNode(1, temp3);
//         }
        return res.next;
    }
    
    private ListNode makeNode(int val, ListNode temp3) {
        ListNode newVal = new ListNode(val);
        temp3.next = newVal;
        temp3 = newVal;
        return temp3;
    }
    
    
}

 


