class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        mod = 10**9 +  7
        n = len(s)
        st =  0
        for i in range(n):
            if s[i] != '1':
                if i > 0 and s[i-1] == '1':
                    k = i-st
                    res += (k * (k+1))//2
                    res %= mod
                else :
                    continue
            else :
                if i > 0 and s[i-1] == '0':
                    st = i
                else:
                    continue
        if n > 1 and s[n-1] == '1':
            k = n-st
            res += k*(k+1)//2
            res %= mod
        return res
                