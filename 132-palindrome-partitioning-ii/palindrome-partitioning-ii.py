class Solution:
    def palindrome(self,s):
        n = len(s)
        arr = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]: arr[i][j] = True
        return arr

    def pp(self, i, s, dp):
        if i >= len(s): return 0
        if dp[i] != -1 : return dp[i]
        minCuts =  float("inf")
        for j in range(i,len(s)):
            if self.palindrome(i,j,s):
                cuts = 1 + self.pp(j+1,s, dp)
                minCuts = min(cuts, minCuts)
        dp[i] = minCuts
        return dp[i]

    def minCut(self, s: str) -> int:
        n = len(s)
        palin = self.palindrome(s)
        dp = [0]*(n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            minCuts =  float("inf")
            for j in range(n-1,i-1,-1):
                if palin[i][j]:
                    cuts = 1 + dp[j+1]
                    minCuts = min(cuts, minCuts)
            dp[i] = minCuts

        return dp[0]-1