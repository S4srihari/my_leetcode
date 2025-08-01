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
        prev  = [[0]*2 for _ in range(3)]
        cur = [[0]*2 for _ in range(3)]
        
        for idx in range(n-1,-1,-1):
            for lim in range(1,3):
                for can_buy in range(2):
                    if can_buy :
                        cur[lim][can_buy] = max(prev[lim][0] - prices[idx], prev[lim][1])
                    else:
                        cur[lim][can_buy] = max(prev[lim-1][1]+prices[idx],prev[lim][0])
            prev,cur = cur,prev
        return prev[2][1]