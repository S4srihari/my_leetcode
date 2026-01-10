class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1), len(s2)
        if m == 0 or n == 0:
            return 0
        tot = 0
        for i in s1:
            tot += ord(i)
        for i in s2:
            tot += ord(i)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m-1,-1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1] + ord(s1[i])*2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return tot - dp[0][0]