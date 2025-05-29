class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        else :
            l,r = 0,0
            for i in range(n-1):
                l,r = r, max(r,l+nums[i])
            u,v = 0,0
            for i in range(n-1):
                u,v = v, max(v,u+nums[i+1])
            return max(r,v)