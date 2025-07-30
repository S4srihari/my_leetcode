class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        prev = [False]*(n+1)
        cur = [False]*(n+1)
        
        prev[n] = True
        j = n-1
        while j > -1 and p[j] == "*":
            prev[j] = True
            j -=1 

        for i in range(m-1,-1,-1):
            cur[n] = False
            for j in range(n-1,-1,-1):
                if s[i] == p[j] or p[j] == '?':
                    cur[j] = prev[j+1]
                elif p[j] == "*":
                    cur[j] =  cur[j+1] or prev[j]
                else:
                    cur[j] = False
            prev,cur = cur,prev
        return prev[0]