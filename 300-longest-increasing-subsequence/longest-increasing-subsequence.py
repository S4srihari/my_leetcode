class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        res = 0
        for i in range(n):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
                res += 1
            else:
                idx = bisect_left(dp,nums[i])
                dp[idx] = nums[i]
        return res