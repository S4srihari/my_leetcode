class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jumps = 0
        cur = 0  
        next_jump = 0
        while cur < len(nums)-1:
            jump_range = nums[cur]+cur
            if jump_range >= len(nums)-1: return jumps+1
            maxi = 0
            for idx in range(cur+1,jump_range+1):
                if nums[idx] + idx > maxi:
                    maxi = idx+nums[idx]
                    next_jump = idx
            jumps += 1
            cur = next_jump
        return jumps
