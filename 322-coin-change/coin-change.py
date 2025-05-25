class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**4+1]*(amount + 1)
        dp[0] = 0
        for x in range(1,amount+1):
            for coin in coins:
                if x>= coin:
                    dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[-1] if dp[-1] != 10**4 + 1 else -1
        