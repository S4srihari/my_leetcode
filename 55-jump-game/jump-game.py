class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = nums[0]
        n = len(nums)
        if maxi >= n-1:
            return True
        idx = 0
        while maxi > idx:
            idx += 1
            maxi = max(maxi,idx+nums[idx])
            if maxi >= n-1:
                return True
        return False 