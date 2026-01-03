class Solution:
    def solve(self, end, cur, form,dp):
        mod = 10**9 + 7
        if cur >= end:
            if form == 1: # Type 1
                return 5
            else:   # type 2
                return 4
        if dp[cur][form-1] != -1:
            return dp[cur][form-1]
        if form == 1:
            dp[cur][form-1] = (self.solve(end, cur+1, 1, dp)*3 + self.solve(end, cur+1, 2, dp)*2)%mod
            return dp[cur][form-1]
        else:
            dp[cur][form-1] = (self.solve(end,cur+1, 1, dp)*2 + self.solve(end, cur+1, 2, dp)*2)%mod
            return dp[cur][form-1]

    def numOfWays(self, n: int) -> int:
        # First Row
        # R Y R, R G R, Y G Y, Y R Y, G R G, G Y G -> Type - 1 (6 ways)
        # R Y G, Y G R, R G Y, Y R G, G R Y, G Y R -> Type - 2 (6 ways)

        # Evaluate both cases from next rows
        # Type 1:  3 Type 1 and 2 Type 2
        # R Y R -> prev
        # Y R G -> 2
        #     Y -> 1
        #   G Y -> 1
        # G R G -> 1
        #     Y -> 2

        # Type 2: 2 Type 1 and 2 Type 2
        # R Y G ->  Prev
        # Y G R -> 2
        #     Y -> 1
        #   R Y -> 1
        # G R Y -> 2

        if n == 1:
            return 12
        tot = 0
        mod = 10**9 + 7
        dp = [[-1]*2 for i in range(n)]
        tot += self.solve(n-1, 1, 1, dp)*6
        tot %= mod
        tot += self.solve(n-1, 1, 2, dp)*6
        tot %= mod
        return tot


