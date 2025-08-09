class Solution:
    def burst(self,nums,left,right,dp):
        if left > right : return 0
        if dp[left][right] != -1: return dp[left][right]
        res = 0
        for idx in range(left,right+1):
            total = nums[idx]*nums[left-1]*nums[right+1] + self.burst(nums,left,idx-1,dp) + self.burst(nums,idx+1,right,dp)
            res = max(res,total)
        dp[left][right] = res
        return dp[left][right]

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[-1]*(n+2) for _ in range(n+2)]
        return self.burst(nums,1,n,dp)