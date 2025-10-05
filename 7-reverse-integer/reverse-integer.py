class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = str(abs(x))[::-1]
        y = int(x)*sign
        return y if y<= 2**31 -1 and y>= -2**31 else 0
