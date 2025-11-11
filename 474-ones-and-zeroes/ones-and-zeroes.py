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
        dp = [[[-1]*(n+1) for _ in range(m+1)] for _ in range(len(strs))]
        return self.solve(len(strs)-1,strs,m,n,dp)