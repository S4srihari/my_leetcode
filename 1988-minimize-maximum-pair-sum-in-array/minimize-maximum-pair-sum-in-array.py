class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[-1]
        for i in range(1,n//2+1):
            ans = max(ans, nums[i] + nums[-(i+1)])
        return ans
        