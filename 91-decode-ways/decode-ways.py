class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        def recurse(idx):
            if idx == n:
                return 1
            if dp[idx] != -1:
                return dp[idx]
            #single
            take1,take2 = 0,0
            if 1<= int(s[idx]) <= 26:
                take1 = recurse(idx+1)
            #double
            if idx <= n-2 and 10<=int(s[idx:idx+2])<=26 :
                take2 = recurse(idx+2)
            dp[idx] = take1 + take2
            return dp[idx]
        return recurse(0)