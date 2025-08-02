class Solution:
    def profit(self,idx,lim,longg,short,prices,n,dp):
        if lim <= 0:
            return 0
        elif idx >= n and short:
            return float("-inf")
        elif idx >= n:
            return 0
        if (idx,lim,longg,short) in dp: return dp[(idx,lim,longg,short)]
        if not longg and not short:
            nothing = self.profit(idx+1,lim,False,False,prices,n,dp)
            enter_long = self.profit(idx+1,lim,True,False,prices,n,dp) - prices[idx] 
            enter_short = self.profit(idx+1,lim,False,True,prices,n,dp) + prices[idx]
            dp[(idx,lim,longg,short)] = max(nothing,enter_long,enter_short)
            return dp[(idx,lim,longg,short)]
        elif longg:
            not_sell = self.profit(idx+1,lim,True,False,prices,n,dp)
            sell = self.profit(idx+1,lim-1,False,False,prices,n,dp) + prices[idx]
            dp[(idx,lim,longg,short)] = max(sell,not_sell)
            return dp[(idx,lim,longg,short)]
        elif short:
            buy = self.profit(idx+1,lim-1,False,False,prices,n,dp) - prices[idx]
            not_buy = self.profit(idx+1,lim,False,True,prices,n,dp)
            dp[(idx,lim,longg,short)] = max(buy,not_buy)
            return dp[(idx,lim,longg,short)]        
       
        
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = {}
        return self.profit(0,k,False,False,prices,n,dp)