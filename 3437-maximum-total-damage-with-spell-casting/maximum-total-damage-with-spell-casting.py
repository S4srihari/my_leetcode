class Solution:    
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        arr =  sorted(c.keys())
        if not arr: return 0
        total = [i*c[i] for i in arr]
        n = len(arr)
        dp = [0]*n
        dp[0] = total[0]
        for i in range(1,n):
            not_take = max(total[i], dp[i-1])
            take = 0
            j = i-1
            while j >= 0 and arr[i]-arr[j] <= 2:
                j-= 1
            if j != -1:
                take = total[i] + dp[j]
            dp[i] = max(not_take, take)

        return dp[n-1] 