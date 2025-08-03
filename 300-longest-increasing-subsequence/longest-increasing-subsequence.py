class Solution:
    def f(self,idx,prev,nums,n,dp):
        if idx >= n:
            return 0
        if dp[idx][prev+1] != None: return dp[idx][prev+1]
        not_take = self.f(idx+1,prev,nums,n,dp)
        take = 0
        if prev == -1 or nums[idx] > nums[prev]:
            take = 1 + self.f(idx+1,idx,nums,n,dp)
        dp[idx][prev+1] = max(take,not_take)
        return dp[idx][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0]*(n+1)
        c = [0]*(n+1)

        for idx in range(n-1,-1,-1):
            for prev in range(idx-1,-2,-1):
                not_take = p[prev+1]
                take = 0
                if prev+1 == 0 or nums[idx] > nums[prev]:
                    take = 1 + p[idx+1]
                c[prev+1] = max(take,not_take)
            p,c = c,p

        return p[0]