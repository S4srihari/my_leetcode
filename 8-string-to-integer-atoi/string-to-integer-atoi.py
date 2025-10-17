class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        i=0
        if s[0] in['+','-']:
            sign=-1 if s[0]=='-' else 1
            i+=1
        num=0
        while i<len(s)and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        num*=sign
        INT_MIN,INT_MAX= -2**31,2**31 -1
        if num <INT_MIN:
            return INT_MIN
        elif num >INT_MAX:
            return INT_MAX
        return num