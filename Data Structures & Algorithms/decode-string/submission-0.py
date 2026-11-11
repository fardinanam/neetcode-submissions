class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            # print(c)
            if not stack:
                if c.isdigit():
                    # print("putting in stack as int")
                    stack.append(int(c))
                else:
                    # print("putting in stack as char")
                    stack.append(c)
            elif c.isdigit():
                if isinstance(stack[-1], int):
                    # print("mult digit")
                    stack[-1] = stack[-1] * 10 + int(c)
                else:
                    # print("new digit")
                    stack.append(int(c))
            elif c == "]":
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop() # pop [
                stack.append(string * stack.pop())
            elif c == "[":
                stack.append(c)
            else:
                if not isinstance(stack[-1], int) and stack[-1] != "[":
                    # print("putting appended string")
                    stack[-1] = stack[-1] + c
                else:
                    # print("putting new char")
                    stack.append(c)
        
        return ''.join(stack)
