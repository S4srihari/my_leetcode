class Solution:
    def subset_sum(self,target, arr):
        dp = [[0]*(target+1) for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][0] = True
        if arr[0] > target: return False
        dp[0][arr[0]] = True 
        for idx in range(1,len(arr)):
            for t in range(target+1):
                not_take = dp[idx-1][t]
                take = False
                if t >= arr[idx]:
                    take = dp[idx-1][t-arr[idx]]
                dp[idx][t] = take or not_take 
        return dp[len(arr)-1][target] is True

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False
        else:
            return self.subset_sum(total_sum//2,nums)
            