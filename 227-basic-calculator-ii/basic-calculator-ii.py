class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i, res = 0, 0
        cur = 0
        cur_operation = '+'
        while i < len(s):
            cur_char = s[i]
            cur = 0
            
            if cur_char.isdigit():
                # find current number
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                
                i -= 1

                if cur_operation == '+':
                    stack.append(cur)
                elif cur_operation == '-':
                    stack.append(-cur)
                elif cur_operation == '*':
                    prev = stack.pop()
                    stack.append(cur * prev)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / cur))

            elif cur_char != ' ':
                cur_operation = cur_char

            i += 1
        
        while stack:
            res += stack.pop()

        return res


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