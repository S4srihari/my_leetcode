class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]  

        for i in range(n-1,-1,-1):
            for buying in [1,0]:
                if buying:
                    buy = dp[i + 1][not buying] - prices[i] if i+1 < n else - prices[i]
                    not_buy  = dp[i + 1][buying]  if i+1 < n else 0
                    dp[i][1] = max(buy, not_buy)
                else:
                    sell = dp[i + 2][not buying] + prices[i]  if i+2 < n else  prices[i]
                    not_sell = dp[i + 1][buying]  if i+1 < n else 0
                    dp[i][0] = max(sell, not_sell)
        return dp[0][1]