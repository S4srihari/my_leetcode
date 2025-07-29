class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s,t = text1, text2
        m, n = len(s),len(t)
        prev = [0]*(n+1)
        cur = [0]*(n+1)

        for idx1 in range(1,m+1):
            for idx2 in range(1,n+1):
                if s[idx1-1] == t[idx2-1]:
                    cur[idx2] = 1 + prev[idx2-1]
                else :
                    cur[idx2] = max(prev[idx2],cur[idx2-1])
            prev,cur = cur,prev

        return prev[n]