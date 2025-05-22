class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        cur = 0
        sign = 1
        stack = [sign]
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == '+' or c == '-':
                res += cur*sign
                sign = (1 if c == '+' else -1)*stack[-1]
                cur = 0
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
        return res + cur*sign