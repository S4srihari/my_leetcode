class Solution:
    def numDecodings(self, s: str) -> int:
        res = [1]
        if s[0] == "0" : return 0
        for i in range(1,len(s)):
            if s[i] == "0" and s[i-1] not in "12":
                return 0
            elif s[i] == "0" or (i+1 < len(s) and s[i+1] == "0"):
                res.append(res[-1])
            elif s[i-1] == "1":
                if res[-1] == 1: res.append(2)
                else : res.append(res[-1]+res[-2])
            elif s[i-1] == "2" and s[i] in "123456":
                if res[-1] == 1: res.append(2)
                else : res.append(res[-1]+res[-2])
            else :
                res.append(res[-1])
        return res[-1]