class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot = sum(nums)
        cur = 0
        res = 0
        for i in range(len(nums)-1):
            cur += nums[i]
            if  abs((tot-cur)-cur)%2 == 0:
                res += 1
        return res