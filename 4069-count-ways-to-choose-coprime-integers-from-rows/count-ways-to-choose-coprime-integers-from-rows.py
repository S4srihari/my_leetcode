class Solution:
    def solve(self, idx, gcd, mat, dp) -> int:
        if idx == self.m:
            return 1 if gcd == 1 else 0
        elif dp[idx][gcd+1] != -1 : return dp[idx][gcd+1]
        ans = 0
        for j in range(self.n):
            if idx == 0:
                ans = (ans + self.solve(idx+1, mat[idx][j], mat, dp))%self.mod
            else:
                ans = (ans + self.solve(idx+1, math.gcd(gcd,mat[idx][j]), mat, dp))%self.mod
        dp[idx][gcd+1] = ans
        return ans

    def countCoprime(self, mat: List[List[int]]) -> int:
        self.mod = 10**9 + 7
        self.m, self.n = len(mat), len(mat[0])
        maxi = 150
        dp = [[-1]*(maxi+2) for _ in range(self.m)]
        return self.solve(0,-1,mat,dp)