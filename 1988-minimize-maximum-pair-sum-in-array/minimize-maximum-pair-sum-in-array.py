class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n//2+1):
            ans = max(ans, nums[i] + nums[-(i+1)])
        return ans
        