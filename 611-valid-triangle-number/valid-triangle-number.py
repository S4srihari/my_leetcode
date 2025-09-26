class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt,n = 0, len(nums)
        for i in range(n-2):
            if nums[i] <= 0: continue
            for j in range(i+1,n-1):
                idx = bisect_right(nums, nums[i]+nums[j]-1)-1
                cnt += idx-j
        return cnt