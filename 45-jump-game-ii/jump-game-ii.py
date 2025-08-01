class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jumps = 0
        cur = 0
        farthest = nums[0]
        for i in range(len(nums)):
            farthest = max(farthest,i+nums[i])
            if i == cur:
                jumps+= 1
                cur = farthest
                if cur >= len(nums)-1:
                    break
        return jumps
