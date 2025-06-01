class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        for i in range(n):
            l,r = r, max(r,l+nums[i])
        return r