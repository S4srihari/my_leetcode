class Solution:
    def solve(self, idx, strs, zeroCnt , oneCnt,dp):
        x = strs[idx].count('0')
        y = strs[idx].count('1')

        if idx == 0:
            return 1 if x <= zeroCnt and y <= oneCnt else 0

        if dp[idx][zeroCnt][oneCnt] != -1: return dp[idx][zeroCnt][oneCnt]

        pick = 0
        if x <= zeroCnt and y <= oneCnt:
            pick = 1 + self.solve(idx-1, strs, zeroCnt-x, oneCnt-y,dp)
        notPick = self.solve(idx-1,strs,zeroCnt,oneCnt,dp)

        dp[idx][zeroCnt][oneCnt] = max(pick,notPick)
        return dp[idx][zeroCnt][oneCnt]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs: return 0
        l = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l)]
        x = strs[0].count('0')
        y = strs[0].count('1')
        for zeroCnt in range(m+1):
            for oneCnt in range(n+1):
                if zeroCnt >= x and oneCnt >= y:
                    dp[0][zeroCnt][oneCnt] = 1

        for idx in range(1,l):
            x = strs[idx].count('0')
            y = strs[idx].count('1')
            for zeroCnt in range(m+1):
                for oneCnt in range(n+1):
                    pick = 0
                    if  x <= zeroCnt and y <= oneCnt:
                        pick = 1 + dp[idx-1][zeroCnt-x][oneCnt-y]
                    notPick = dp[idx-1][zeroCnt][oneCnt]
                    dp[idx][zeroCnt][oneCnt] = max(pick,notPick)

        return dp[l-1][m][n]