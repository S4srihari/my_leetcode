class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left <= right:
            mid = left + (right - left )//2
            cnt, last_pos = 0, -2
            for i in range(len(nums)):
                if nums[i] <= mid and i-last_pos > 1:
                    cnt += 1
                    last_pos = i
            if cnt < k:
                left = mid + 1
            else :
                right = mid - 1
        return left