class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prev = [float("inf")]*(amount+1)
        prev[0] = 0
        for coin in coins:
            if coin > amount: continue
            for change in range(coin,amount+1):
                prev[change] = min(prev[change-coin]+1,prev[change])
        return prev[-1] if prev[-1] != float("inf") else -1
        