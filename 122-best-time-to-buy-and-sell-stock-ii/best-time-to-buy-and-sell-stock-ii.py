class Solution:
    def profit(self,idx,n,can_buy,prices,dp):
        if idx >= n:
            return 0
        if dp[idx][can_buy] != -1: return dp[idx][can_buy]
        if can_buy :
            dp[idx][can_buy] = max(self.profit(idx+1,n,can_buy,prices,dp),self.profit(idx+1,n,0,prices,dp)-prices[idx])
            return dp[idx][can_buy]
        else:
            dp[idx][can_buy] = max(self.profit(idx+1,n,can_buy,prices,dp),self.profit(idx+1,n,1,prices,dp)+prices[idx])
            return dp[idx][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        prev_buy,prev_not_buy = 0,0 
        cur_buy, cur_not_buy = 0,0
        for idx in range(n-1,-1,-1):
            cur_buy = max(prev_buy,prev_not_buy-prices[idx])
            cur_not_buy = max(prev_not_buy,prev_buy+prices[idx])
            prev_buy,prev_not_buy = cur_buy,cur_not_buy
        return prev_buy