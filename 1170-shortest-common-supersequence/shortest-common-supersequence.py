class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        a,b = str1, str2
        m,n = len(a),len(b)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        res = []
        i,j = m,n
        while i > 0 and j > 0:
            if a[i-1] == b[j-1]:
                res.append(a[i-1])
                i,j = i-1,j-1
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(a[i-1])
                i -= 1
            else :
                res.append(b[j-1])
                j -= 1

        while i > 0:
            res.append(a[i-1])
            i -= 1
        while j > 0:
            res.append(b[j-1])
            j -= 1
        
        return "".join(res[::-1]) 