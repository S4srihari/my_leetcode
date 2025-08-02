class Solution:
    def profit(self,idx,n,can_buy,prices,dp):
        if idx >= n:
            return 0
        if dp[idx][can_buy] != -1: return dp[idx][can_buy]
        if can_buy :
            dp[idx][can_buy] = max(self.profit(idx+1,n,can_buy,prices,dp),self.profit(idx+1,n,not can_buy,prices,dp)-prices[idx])
            return dp[idx][can_buy]
        else:
            dp[idx][can_buy] = max(self.profit(idx+1,n,can_buy,prices,dp),self.profit(idx+1,n,not can_buy,prices,dp)+prices[idx])
            return dp[idx][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        dp = [[-1]*2 for _ in range(n)]
        return self.profit(0,n,True,prices,dp) 