class Solution:
    def profit(self,idx,can_buy,prices,lim,n,dp):
        if lim == 0:
            return 0
        if idx == n:
            return 0
        if dp[idx][lim][can_buy] != None: return dp[idx][lim][can_buy]
        if can_buy :
            dp[idx][lim][can_buy] = max(self.profit(idx+1,0,prices,lim,n,dp) - prices[idx], self.profit(idx+1,1,prices,lim,n,dp))
            return dp[idx][lim][can_buy]
        else:
            dp[idx][lim][can_buy] = max(self.profit(idx+1,1,prices,lim-1,n,dp)+prices[idx],self.profit(idx+1,0,prices,lim,n,dp))
            return dp[idx][lim][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[None]*2 for _ in range(3)] for _ in range(n+1)]
        for i in range(3):
            for j in range(2):
                dp[n][i][j] = 0
        for i in range(n+1):
            for j in range(2):
                dp[i][0][j] = 0
        
        for idx in range(n-1,-1,-1):
            for lim in range(3):
                for can_buy in range(2):
                    if can_buy :
                        dp[idx][lim][can_buy] = max(dp[idx+1][lim][0] - prices[idx], dp[idx+1][lim][1])
                    else:
                        if lim > 0:
                            dp[idx][lim][can_buy] = max(dp[idx+1][lim-1][1]+prices[idx],dp[idx+1][lim][0])
                        else :
                            dp[idx][lim][can_buy] = dp[idx+1][lim][0]
        return dp[0][2][1]