class Solution:
    def calculate(self, s: str) -> int:
        # T: O(n), S: O(n)
        stack = []
        cur = 0
        cur_operation = '+'

        def helper(op, cur):
            match op:
                case '+':
                    stack.append(cur)
                case '-':
                    stack.append(-cur)
                case '*':
                    stack.append(stack.pop() * cur)
                case '/':
                    stack.append(int(stack.pop() / cur))

        for cur_char in s:
            if cur_char.isdigit():
                cur = cur * 10 + int(cur_char)
            elif cur_char in '+-*/':
                helper(cur_operation, cur)
                
                cur = 0
                cur_operation = cur_char

        helper(cur_operation, cur)

        return sum(stack)


2
3

        # T: O(n), S: O(1), undoing previous action
        # i = 0

        # # 3+2*2
        # #     i

        # # cur 2
        # # prev 4
        # # res 7
        # # cur_opr *

        # cur = prev = res = 0
        # cur_operation = '+'

        # while i < len(s):
        #     cur_char = s[i]

        #     # 3 cases, digit, math operation, and whitespace
        #     if cur_char.isdigit():
        #         while i < len(s) and s[i].isdigit():
        #             cur = cur * 10 + int(s[i])
        #             i += 1
            
        #         i -= 1

        #         if cur_operation == '+':
        #             res += cur
        #             prev = cur
        #         elif cur_operation == '-':
        #             res -= cur
        #             prev = -cur
        #         elif cur_operation == '*':
        #             res -= prev
        #             res += prev * cur
        #             prev = cur * prev
        #         else:
        #             res -= prev
        #             res += int(prev / cur)
        #             prev = int(prev / cur)
                
        #         cur = 0
            
        #     elif cur_char != ' ':
        #         cur_operation = cur_char
            
        #     i += 1
        
        # return res