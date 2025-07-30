class Solution:
    def subs(self,i,j,s,t,dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1: return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.subs(i-1,j-1,s,t,dp) + self.subs(i-1,j,s,t,dp)
            return dp[i][j]
        else:
            dp[i][j] = self.subs(i-1,j,s,t,dp)
            return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        if m < n:
            return 0
        dp = [[-1]*(n) for i in range(m)]
        return self.subs(m-1,n-1,s,t,dp)