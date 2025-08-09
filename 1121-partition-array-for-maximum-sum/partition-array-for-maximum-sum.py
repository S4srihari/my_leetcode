class Solution:
    def partition(self,idx,start,arr,k,n,dp):
        if idx == n and start < n: return max(arr[start:idx])*(idx-start)
        elif idx == n: return 0
        if (idx,start) in dp: dp[(idx,start)]
        if idx-start+1 == k:
            dp[(idx,start)] = self.partition(idx+1,idx+1,arr,k,n,dp)+ max(arr[start:idx+1])*k
            return dp[(idx,start)]
        else:
            not_part = self.partition(idx+1,start,arr,k,n,dp)
            part = self.partition(idx+1,idx+1,arr,k,n,dp) + max(arr[start:idx+1])*(idx-start+1)
            dp[(idx,start)] = max(part,not_part)
            return dp[(idx,start)]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[float("-inf")]*(n+1) for _ in range(n+1)]
        dp[n][n] = 0
        cur_max = float("-inf")
        for start in range(n-1,n-k-1):
            cur_max = max(cur_max,arr[start])
            dp[n][start] =  cur_max*(n-start)

        for idx in range(n-1,-1,-1):
            cur_max = float("-inf")
            for start in range(idx,max(-1,idx-k),-1):
                cur_max = max(cur_max,arr[start])
                not_part = dp[idx+1][start]
                part = dp[idx+1][idx+1] + cur_max*(idx-start+1)
                dp[idx][start] = max(part,not_part)

        return dp[0][0]