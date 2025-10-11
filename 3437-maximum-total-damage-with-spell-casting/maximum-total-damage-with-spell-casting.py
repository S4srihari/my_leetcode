class Solution:
    def helper(self, idx, arr, prev, n, dp):
        if idx < 0: return 0
        if dp[idx][prev] != -1: return dp[idx][prev]
        not_take = self.helper(idx-1,arr, prev, n, dp)
        take = -1
        if prev == n or arr[prev][0] - arr[idx][0] > 2:
            take = arr[idx][1] + self.helper(idx-1,arr,idx,n, dp)
        dp[idx][prev] = max(take,not_take)
        return dp[idx][prev]
        
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