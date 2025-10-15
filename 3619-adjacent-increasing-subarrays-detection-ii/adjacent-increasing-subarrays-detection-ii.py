class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        elif n < 4: return 1 
        res = 1
        forward = [1]*n
        backward = [1]*n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                forward[i] = forward[i-1] + 1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                backward[i] = backward[i+1] + 1
        
        for i in range(1,n):
            cur = min(forward[i-1],backward[i])
            res = max(res, cur)
        return res