class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i is ")":
                reversed = ""
                while not stack[-1] == "(":
                    reversed += stack.pop()
                stack.pop()
                for j in reversed:
                    stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)
