class Solution:
    def myAtoi(self, s: str) -> int:
        st = s.strip()
        res = 0
        sign = 1
        seq = False
        valid = ['0','1','2','3','4','5','6','7','8','9','-','+']
        for c in st:
            if c not in valid:
                break
            elif (c == '-' or c =='+') and (sign == -1 or seq):
                break
            elif c == '-':
                sign = -1
                seq = True
            elif c == '+':
                sign = 1
                seq = True
            else:
                res *= 10 
                res += int(c)
                seq = True
        if res >= 2**31 and sign == -1: return -2**31
        elif res > 2**31-1 : return 2**31 - 1
        return res*sign