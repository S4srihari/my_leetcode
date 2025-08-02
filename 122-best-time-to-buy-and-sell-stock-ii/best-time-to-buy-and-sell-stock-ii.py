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
        prev = [0]*2 
        cur = [0]*2
        for idx in range(n-1,-1,-1):
            for can_buy in range(2):
                if can_buy :
                    cur[can_buy] = max(prev[can_buy],prev[0]-prices[idx])
                else:
                    cur[can_buy] = max(prev[can_buy],prev[1]+prices[idx])
            prev,cur = cur,prev
        return prev[1]